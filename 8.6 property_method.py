class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError("can't del attribute")

    # 根据已存在的get/set方法生成property
    name = property(get_first_name, set_first_name, del_first_name)


a = Person('lijiachang')

print(a.name)
a.name = 123
del a.name
