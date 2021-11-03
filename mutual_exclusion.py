import threading
import time

count = 0
my_lock = threading.Lock()


def increment_count():
    global count
    for i in range(5):
        print(threading.current_thread().getName(), 'is thinking.')
        time.sleep(0.5)
        my_lock.acquire()
        count += 1
        my_lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=increment_count)
    t2 = threading.Thread(target=increment_count)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Count:', count)
