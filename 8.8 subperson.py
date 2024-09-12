class Person:
    def __init__(self, name):
        self.name = name  # 在初始化阶段就可以执行检查

    # getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # deleter
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):

    @property
    def name(self):
        print('getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)  # 注意这里是用的__set__

    @name.deleter
    def name(self):
        print('deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)  # 注意这里是用的__delete__


sub = SubPerson('lijiachang')
print(sub.name)
sub.name = 'new name'

sub.name = 18


class SubPerson(Person):

    # @Person.name.getter
    # @Person.name.setter
    @Person.name.deleter
    def name(self):
        print('deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)
