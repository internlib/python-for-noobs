
# 0 , 1, 1, 2, 3, 5, 8, 13 ..
import time


def fibonacci(amount):
    result = [0, 1]
    for _ in range(amount -2):
        result.append(sum(result[-2:])) 
    return result


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
