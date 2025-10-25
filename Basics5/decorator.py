import time

def measure_time(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print("Время выполнения функции: ", end_time - start_time)
        return result
    return wrapper

@measure_time
def summa(a, b):
    print("Результат сложения: ", a + b)

@measure_time
def file_sum():
    with open('input.txt', 'r') as f:
        a, b = map(float, f.readline().split())
        result = a + b
    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == '__main__':
    summa(2, 3)
    file_sum()
