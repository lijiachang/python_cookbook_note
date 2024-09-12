class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self.a = A()

    def bar(self):
        pass

    def __getattr__(self, item):
        """暴露所有A的方法"""
        getattr(self.a, item)
