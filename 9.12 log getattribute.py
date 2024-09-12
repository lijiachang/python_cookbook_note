def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print('getting: ', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls

@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass

a = A(12)
a.x
a.spam()

class LoggedGetAttribute:
    def __getattribute__(self, item):
        print('getting: ', item)
        return super().__getattribute__(item)


class A(LoggedGetAttribute):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass