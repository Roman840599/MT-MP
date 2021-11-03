import random
import threading
import time

my_semaphore = threading.Semaphore(1)


def take_toilet_cabin():
    name = threading.current_thread().getName()
    with my_semaphore:
        print(name, 'is in...')
        time.sleep(random.uniform(1, 2))
        print(name, 'is out, FREE!')


if __name__ == '__main__':
    for person in range(10):
        threading.Thread(target=take_toilet_cabin, name='Person-'+str(person)).start()
