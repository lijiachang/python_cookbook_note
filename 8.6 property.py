class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """检查为string类型"""
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        """不允许删除属性"""
        raise AttributeError("Can't delete attribute")


print(Person.first_name.fget)
print(Person.first_name.fset)
print(Person.first_name.fdel)