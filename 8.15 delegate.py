class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self.a = A()

    def spam(self, x):
        return self.a.spam(x)

    def foo(self):
        return self.a.foo()

    def bar(self):
        pass