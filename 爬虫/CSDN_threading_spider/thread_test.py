import time
import threading


def sleep_task(seconds):
    print('sleep {} seconds start!'.format(seconds))
    time.sleep(seconds)
    print('sleep {} seconds end!'.format(seconds))


if __name__ == '__main__':
    t1 = threading.Thread(target=sleep_task, args=(2,))
    t1.setDaemon(True)  # 守护线程
    t1.start()
    t2 = threading.Thread(target=sleep_task, args=(3,))
    t2.setDaemon(True)
    t2.start()

    # t1.join()  # 阻塞，直到t1运行完毕
    # t2.join()  # 同理

    time.sleep(2)