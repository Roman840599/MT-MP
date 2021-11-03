import datetime
from threading import Thread


def count_factorial(number):
    print('started counting ', number)
    result = 1
    for i in range(2, number+1):
        result = result * i
    return result


if __name__ == '__main__':
    p1 = Thread(target=count_factorial, args=(555555,))
    p2 = Thread(target=count_factorial, args=(555533,))
    start = datetime.datetime.now()
    print(f'Start counting at {start}.')
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    finish = datetime.datetime.now()
    delta = finish - start
    print(f'Finished counting at {finish}, timedelta {delta}')
