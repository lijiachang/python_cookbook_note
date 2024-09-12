class NoMixedCaseMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        for name in cls_dict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, cls_name, bases, cls_dict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):
    def foo_bar(self):
        pass


class B(Root):
    def fooBar(self):  # TypeError: Bad attribute name: fooBar
        pass
