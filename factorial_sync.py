import datetime


def timer(f):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        print(f'Start counting {f} at {start}.')
        res = f(*args, **kwargs)
        finish = datetime.datetime.now()
        delta = finish - start
        print(f'Finished counting {f} at {finish}, timedelta {delta}')
        return res
    return wrapper


@timer
def count_three_numbers(number1, number2):
    res1 = count_factorial(number1)
    res2 = count_factorial(number2)
    return res2 + res1


def count_factorial(number):
    result = 1
    for i in range(2, number+1):
        result = result * i
    return result


if __name__ == '__main__':
    start = datetime.datetime.now()
    print(f'Start counting at {start}.')
    count_factorial(555555)
    count_factorial(555533)

    finish = datetime.datetime.now()
    delta = finish - start
    print(f'Finished counting at {finish}, timedelta {delta}')
