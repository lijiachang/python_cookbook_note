class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, new_state):
        self.__class__ = new_state

    def read(self):
        raise NotImplementedError

    def write(self, data):
        raise NotImplementedError

    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class ClosedConnection(Connection):

    def read(self):
        raise RuntimeError('Not open')

    def write(self, data):
        raise RuntimeError('Not open')

    def open(self):
        self.new_state(OpenedConnection)

    def close(self):
        raise RuntimeError('Already closed')


class OpenedConnection(Connection):

    def read(self):
        print('reading')

    def write(self, data):
        print('writing')

    def open(self):
        raise RuntimeError('Already write')

    def close(self):
        self.new_state(ClosedConnection)

c = Connection()
print(c)

c.open()
c.read()
c.write('hello')
c.close()

c.read()