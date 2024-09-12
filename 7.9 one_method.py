from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


yahoo = urltemplate('http://xxx.com/quotes.csv?s={name}&f{fileds}')
for line in yahoo(name='IBM,AAPL', fileds='sl1c1v'):
    print(line.decode('utf-8'))
