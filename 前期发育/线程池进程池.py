from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
                                #线程池              #进程池
def fn():
    for i in range(1000):
        print(i)

with ThreadPoolExecutor(50) as t:
    #把ThreadPoolExecutor改成ProcessPoolExecutor就变成进程池了
    #50个线程池去处理fn函数这个任务
    t.submit(fn)
print(123)

