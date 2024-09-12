import time


def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


from threading import Thread

t = Thread(target=countdown, args=(10,))
# 当创建一个线程实例时，在调用它的start方法之前，线程不会立即开始执行
t.start()
# 现场实例会在它们所属的系统级线程（即，POSIX线程或Windows线程）中执行，这些线程完全由操作系统来管理。
# 一旦启动后，线程开始独立运行，直到目标函数返回为止

# 查询线程是否还在运行
print(t.is_alive())

# 也可以请求连接（join）到某个线程上，这么做会等待该线程结束：
t.join()
# 解释器会一直保持运行，直到所有线程都终结为止。

# # 对于需要长时间运行的线程或者一直不断运行的后台任务，应该考虑将这些线程设置为daemon
# t = Thread(target=countdown, args=(10,), daemon=True)
# # dem