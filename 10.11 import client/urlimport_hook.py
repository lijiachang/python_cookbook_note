import sys
import importlib.abc
import imp
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser
from typing_extensions import Literal, TypeAlias

from typing import Optional, List, Tuple, Sequence
# debugging
import logging

# 配置日志
# 第一步：创建日志器对象，默认等级为warning
log = logging.getLogger(__name__)
logging.basicConfig(level="DEBUG")
# 第二步：创建控制台日志处理器
console_handler = logging.StreamHandler()
# 第三步：设置控制台日志的输出级别,需要日志器也设置日志级别为info；----根据两个地方的等级进行对比，取日志器的级别
console_handler.setLevel(level="DEBUG")
# 第四步：设置控制台日志的输出格式
console_fmt = "%(name)s--->%(asctime)s--->%(message)s--->%(lineno)d"
fmt1 = logging.Formatter(fmt=console_fmt)
console_handler.setFormatter(fmt=fmt1)
# 第五步：将控制台日志器，添加进日志器对象中
log.addHandler(console_handler)

_Path: TypeAlias = bytes | str


def _get_links(url):
    """访问提供的url，解析出HTML中的链接"""
    links = set()

    class LinkParser(HTMLParser):
        def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
            if tag == "a":
                attrs = dict(attrs)
                links.add(attrs.get('href').rstrip('/'))

    try:
        log.debug('getting links from %s', url)
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode('utf-8'))
    except Exception as e:
        log.debug('could not get links. %s', e)

    log.debug('links: %r', links)
    print(links)
    return links


class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links = {}
        self._loaders = {baseurl: UrlModuleLoader(baseurl)}

    def find_module(self, fullname: str, path: Optional[Sequence[_Path]] = None) -> Optional[importlib.abc.Loader]:
        log.debug('find_module: fullname=%r, path=%r', fullname, path)
        if path is None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]

        parts = fullname.split('.')
        basename = parts[-1]
        log.debug('find_module: baseurl=%r, basename=%r', baseurl, basename)

        # 检查链接缓存
        if basename not in self._links:
            self._links[baseurl] = _get_links(baseurl)

        # 检查是否 package
        if basename in self._links[baseurl]:
            log.debug('find_module: trying package %r', fullname)
            fullurl = self._baseurl + '/' + basename
            # 尝试加载模块（访问 __init__.py)
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug('find_module: package %r loaded', fullname)
            except ImportError as e:
                log.debug('find_module: package failed. %s', e)
                loader = None
            return loader

        filename = basename + '.py'
        if filename in self._links[baseurl]:
            log.debug('find_module: module %r found', fullname)
            return self._loaders[baseurl]
        else:
            log.debug('find_module: module %r not found', fullname)
            return None
    def invalidate_caches(self) -> None:
        log.debug('invalidating(使无效，废除) link cache')
        self._links.clear()


class UrlModuleLoader(importlib.abc.SourceLoader):
    """用于加载URL模块的模块加载器"""

    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}

    def module_repr(self, module):
        return '<urlmodule %r from %r>' % (module.__name__, module.__file__)

    # required method:
    def load_module(self, fullname):
        """"""
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition('.')[0]

        exec(code, mod.__dict__)
        return mod

    # optional extensions:
    def get_code(self, fullname):
        """"""
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), 'exec')

    def get_data(self, path):
        pass

    def get_filename(self, fullname):
        return self._baseurl + '/' + fullname.split('.')[-1] + '.py'

    def get_source(self, fullname):
        filename = self.get_filename(fullname)
        log.debug('loader: reading %r', filename)
        if filename in self._source_cache:
            log.debug('loader: cached %r', filename)
            return self._source_cache[filename]
        try:
            u = urlopen(filename)
            source = u.read().decode('utf-8')
            log.debug('loader: %r loaded', filename)
            self._source_cache[filename] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug('loader: %r failed, error: %s', filename, e)
            raise ImportError(f'Cant load {filename}')

    def is_package(self, fullname):
        return False


class UrlPackageLoader(UrlModuleLoader):
    """从url加载package"""

    def load_module(self, fullname):
        mod = super().load_module(fullname)
        mod.__path__ = [self._baseurl]
        mod.__package__ = fullname

    def get_filename(self, fullname):
        return self._baseurl + '/' + '__init__.py'

    def is_package(self, fullname):
        return True

class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._links = None
        self._loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl

    def find_loader(self, fullname):
        log.debug('find_loader: %r', fullname)
        parts = fullname.split('.')
        basename = parts[-1]

        # 检查链接缓存
        if self._links is None:
            self._links = []  # todo 解释?
            self._links = _get_links(self._baseurl)

        # 检查是否package
        if basename in self._links:
            log.debug('find_loader: trying package %r', fullname)
            full_url = self._baseurl + '/' + basename
            # 尝试加载package(访问__init__.py)
            loader = UrlPackageLoader(full_url)
            try:
                loader.load_module(fullname)
                log.debug('find_loader: package %r loaded', fullname)
            except ImportError as e:
                log.debug('find_loader: %r is a namespace package', fullname)
                loader = None
            return (loader, [full_url])
        # 正常的模块(脚本)
        filename = basename + '.py'
        if filename in self._links:
            log.debug('find_loader: module %r found', fullname)
            return (self._loader, [])
        else:
            log.debug('find_loader: module %r not found', fullname)
            return (None, [])

    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links = None

_url_path_cache = {}
def handler_url(path):
    if path.startswith(('http://', 'https://')):
        log.debug('Handler path? %s. [Yes]', path)
        if path in _url_path_cache:
            finder = _url_path_cache[path]
        else:
            finder = UrlPathFinder(path)
            _url_path_cache[path] = finder
        return finder
    else:
        log.debug('Handler path? %r. [No]', path)


def install_path_hook():
    sys.path_hooks.append(handler_url)
    sys.path_importer_cache.clear()
    log.debug('Installing handler_url')

def remove_path_hook():
    sys.path_hooks.remove(handler_url)
    sys.path_importer_cache.clear()
    log.debug('Removing handler_url')