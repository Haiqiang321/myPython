# _*_ coding:utf-8 _*_
import threading


# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py

def test(value1, value2=None):
    print("%s threading is printed %s, %s" % (threading.current_thread().name, value1, value2))


#     time.sleep(2)


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor

    threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
    for i in range(0, 10):
        #         test(str(i), str(i+1))
        threadPool.map(test, [i],
                       [i + 1])  # 这是运行一次test的参数，众所周知map可以让test执行多次，即一个[]代表一个参数，一个参数赋予不同的值即增加[]的长度如从[1]到[1,2,3]
    threadPool.shutdown(wait=True)


