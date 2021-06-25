# Чтобы запустить код проскрольте в конец
import math


def one(n, i=1):
    if n == i:
        print("Задание 1")
        return (n + 1)/(2 * n + 5)
    else:
        return (i + 1)/(2 * i + 5) + one(n, i + 1)


def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)


def two_recursion(x, epsilon=0.001, i=0):
    if i == 0:
        a = 1
    else:
        a = (x**i)/(factorial(i))

    if a < epsilon:
        print("Задание 2, рекурсивный метод")
        print(f"кількість членів яку ряду необхідно підсумувати для досягнення зазначеної точності = {i+1}")
        print(f"e^x = {math.e ** x}")
        print("result = ", end="")
        return 0
    else:
        return a + two_recursion(x, epsilon, i + 1)


def two_iteration(x, epsilon=0.001):
    result = 0
    i = 0
    a = 1
    while a > epsilon:
        if i != 0:
            fact = i
            j = i
            while j > 1:
                j -= 1
                fact *= j
            a = (x**i)/fact
        if a > epsilon:
            result += a
        i += 1
    print("Задание 2, итеративный метод")
    print(f"кількість членів яку ряду необхідно підсумувати для досягнення зазначеної точності = {i}")
    print(f"e^x = {math.e ** x}")
    print("result = ", result)


if __name__ == '__main__':
    #Запускайте функции тут
    print(one(10))
    print(two_recursion(3))
    two_iteration(3)
