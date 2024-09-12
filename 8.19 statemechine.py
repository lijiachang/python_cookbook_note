class ConnectionState:
    """基类"""

    @staticmethod
    def read(conn):
        raise NotImplementedError

    @staticmethod
    def write(conn, data):
        raise NotImplementedError

    @staticmethod
    def open(conn):
        raise NotImplementedError

    @staticmethod
    def close(conn):
        raise NotImplementedError


class ClosedConnectionState(ConnectionState):
    """关闭状态"""

    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class OpenConnectionState(ConnectionState):
    """开启状态"""

    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already opened')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, new_state):
        self._state = new_state

    # 委托到状态机
    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


c = Connection()
print(c._state)
c.open()
print(c._state)

c.read()
c.write('hello')
c.close()
print(c._state)
c.read()