import threading


# THREAD_NUM自定义全局变量需要执行的线程数
# ONE_WORKER_NUM自定义每个线程循环次数
# 这两个变量乘积就是并发数
THREAD_NUM = 1
ONE_WORKER_NUM = 1

# 自定义需要执行的test() 函数，可以是多个
def test():
    #测试代码


# 引用全局变量作为循环执行的次数，嵌套执行指定循环次数的test()函数
def working():
    global ONE_WORKER_NUM
    for i in range(0,ONE_WORKER_NUM):
        test()


def t():
		# 自定义t()作为多线程并发的函数
		# 并将working()函数放入线程之中，这样每个线程都可以执行多次test()函数
		# 给所有创建的子线程设置守护线程
    global THREAD_NUM
    Threads = []
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working,name="T" + str(i))
        t.setDaemon(True)
        Threads.append(t)
		# 循环启动
    for t in Threads:
        t.start()
		# 循环对线程组中的每个线程设置阻塞线程
    for t in Threads:
        t.join()

# 通过主线程启动t()中的子线程
if __name__ == "__main__":
    t()
		
		
# 所有子线程结束之后，可以执行其他代码，比如对文件写入结果等
