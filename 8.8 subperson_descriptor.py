class String:
    """描述符"""

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(instance.__dict__)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Can't delete attr")


class Person:
    """带有描述符的类"""
    name = String('name')

    def __init__(self, name):
        self.name = name


class SubPerson(Person):
    @property
    def name(self):
        print('getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('setting name')
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


sub = SubPerson('lijiachang')
sub.name = 'new name'
del sub.name
