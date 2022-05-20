import time


def measureTime(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        total = time.time() - start
        print(total, "segundos")

        return result

    return wrapper


@measureTime
def suma(a, b):
    time.sleep(1)
    s = a + b
    return s


print(suma(10, 30))
