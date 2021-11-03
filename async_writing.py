import threading
import time


my_lock = threading.Barrier(2)


def plus_number():
    while True:
        with open('example.txt', 'r') as text_file:
            value = int(text_file.read())
            new_value = value + 1
        with open('example.txt', 'w') as text_file:
            text_file.write(f"{str(new_value)}")
            print(f'performed {value} + 1, written {new_value}')
        my_lock.wait()
        time.sleep(0.1)


def minus_number():
    while True:
        my_lock.wait()
        with open('example.txt', 'r') as text_file:
            value = int(text_file.read())
            new_value = value - 1
        with open('example.txt', 'w') as text_file:
            text_file.write(f"{str(new_value)}")
            print(f'performed {value} - 1, written {new_value}')
        time.sleep(0.1)


if __name__ == '__main__':
    t1 = threading.Thread(target=plus_number)
    t2 = threading.Thread(target=minus_number)
    t1.start()
    t2.start()
