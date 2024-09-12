class RestrictKeysMixin:
    """检查key是否是指定类型"""

    def __init__(self, *args, _restrict_key_type, **kwargs):
        self._restrict_key_type = _restrict_key_type
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(key, self._restrict_key_type):
            raise TypeError('Key must be ' + str(self._restrict_key_type))
        super().__setitem__(key, value)  # 按照mro的顺序，会委托给dict的setitem方法，所以要把mixin类的继承顺序放到前面


class RDict(RestrictKeysMixin, dict):
    pass


d = RDict(_restrict_key_type=str)
e = RDict([('name', 'lijiachang'), ('age', 28)], _restrict_key_type=str)
f = RDict(name='lijiachang', age=28, _restrict_key_type=str)

print(f)
f[10] = 123
