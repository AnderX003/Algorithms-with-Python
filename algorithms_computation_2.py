from random import randint
import operator
from math import log


def _01(k, n):
    """функция получает максимальную длину шага, финальную точку и
    возвращает колличество путей и ней"""
    counter = k
    lst = [0, 1] + [0] * n
    for i in range(2, n + 2):
        while counter > 0:
            lst[i] += lst[i - counter]
            counter -= 1
        counter = k
    return lst[n + 1]


def _02(k, n):
    """функция получает максимальную длину шага, финальную точку
    на каждой точке можно потерять или заработать деньги.
    функция расчитывает максимальное количество прибыли
    при достижении финальной точки"""
    prices = [randint(-5, 5) for _ in range(0, n + 1)]
    prices[0] = 0
    print(prices)
    lst = [0] * (n + 1)
    if prices[1] > 0:
        lst[1] = prices[1]
    for i in range(2, n + 1):
        counter = 1
        local_list = []
        while counter != k + 1:
            local_list.append(lst[i - counter])
            counter += 1
        lst[i] = max(local_list) + prices[i]
    return lst[n]


def _03(k, n, min_price, max_price):
    """функция получает максимальную длину шага, финальную точку
    на каждой точке можно потерять или заработать деньги.
    функция расчитывает максимально прибыльный путь к финальной точке"""
    # prices = [0, 2, 4, -1, 4, -2, -1, 3, 4, -2, -2]
    prices = [randint(min_price, max_price) for _ in range(0, n + 1)]
    prices[0] = 0
    print(prices)
    pos = 0
    money = 0
    steps_indexes = [0]
    bad_things = False  # последний элемент отрицательный
    if prices[n] < 0:
        bad_things = True
    while True:
        for e in range(1, k + 1):
            if bad_things and e > n - pos:
                money += prices[n]
                pos = n
                steps_indexes.append(pos)
                break
            if prices[pos + e] >= 0:
                money += prices[pos + e]
                pos += e
                steps_indexes.append(pos)
                break
            elif e == k:
                can_do_steps = [prices[pos + j] for j in range(1, k + 1)]
                max_point = max(can_do_steps)
                index = can_do_steps[::-1].index(max_point)
                max_point_index = k - index
                money += prices[pos + max_point_index]
                pos += max_point_index
                steps_indexes.append(pos)
        if pos == n:
            break
    return steps_indexes  # список индексов, на которые пошёл коник


def _04_a():
    """Функция возвращает максимальную ценность, которую может иметь рюкзак.
    (предметы могут повторяться)"""
    w = 80
    items = ((90, 30), (60, 15), (100, 50), (15, 10), (20, 15))  # Price - weight
    n = len(items)
    print('Предметы:')
    for k in range(n):
        print(f'{k + 1}) цена {items[k][1]} вес {items[k][0]}')
    worth = [x / y for x, y in items]
    sorted_index_of_worth = sorted([i for i in range(len(worth))], key=lambda k: worth[k], reverse=True)
    current_weight = 0
    total_price = 0
    for i in sorted_index_of_worth:
        while current_weight + items[i][1] <= w:
            current_weight += items[i][1]
            total_price += items[i][0]
            print(f'Украден предмет, ценой {items[i][0]}, и веса {items[i][1]}')
    return total_price


def _04_b():
    """Функция возвращает максимальную ценность, которую может иметь рюкзак.
    (предметы НЕ могут повторяться)"""
    weight = (30, 15, 50, 10, 15)
    price = (90, 60, 100, 15, 20)
    W = 80
    n = len(price)

    print('Предметы:')
    for k in range(n):
        print(f'{k + 1}) цена {price[k]} вес {weight[k]}')

    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(price[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    print('\nЗаполнение рюкзака:')
    w, i, total_weight = W, n, 0
    res = K[n][W]
    total_price = 0
    while i > 0 and res > 0:
        if res != K[i - 1][w]:
            print(f'{i}-й предмет, ценой {price[i - 1]} и веса {weight[i - 1]}')
            total_price += price[i - 1]
            total_weight += weight[i - 1]
            res -= price[i - 1]
            w -= weight[i - 1]
        i -= 1

    print('Всего украдено на:', total_price)


def _05(m=4, n=4):
    """Функция возвращает минимальную цену, за которую
    король может дойти до точки (m, n)."""
    price = ((6, 2, 7, 9, 9), (0, 8, 6, 7, 0), (3, 6, 3, 0, 6), (2, 9, 2, 8, 8), (1, 9, 9, 8, 7))
    INF = 20 ** 30
    result = [[0] * (m + 1) for _ in range(n + 1)]
    result[0][0] = 0
    for i in range(1, n + 1):
        result[i][0] = INF
    for j in range(1, m + 1):
        result[0][j] = INF
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            result[i][j] = min(result[i][j - 1], result[i - 1][j], result[i - 1][j - 1]) + price[i][j]
    return result[m][n]


def _06(m=4, n=4):
    """Функция возвращает траэкторию, пройдя по которой,
    котоль заплатит минимальную цену, чтобы дойти до точки (m, n)."""
    G = ((1, 2, 3, 4, 5), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5))
    result = []
    i = n
    j = m
    while (i, j) != (0, 0):
        result.append((i, j))
        prev_G = min(G[i][j - 1], G[i - 1][j], G[i - 1][j - 1])
        if G[i][j - 1] == prev_G:
            i, j = i, j - 1
        elif G[i - 1][j] == prev_G:
            i, j = i - 1, j
        else:
            i, j = i - 1, j - 1
    result = result[::-1]
    return result


def _07(n):
    """Функция возвращает количество интерпритаций
    из n цифр, в которых нет трёх единиц подряд."""
    def rec(n_, rez=""):
        counter = 0
        if n_ > 0:
            for i in ["0", "1"]:
                counter += rec(n_ - 1, rez + i)
        else:
            if "111" in rez:
                return 1
        return counter
    return 2**n - rec(n)


def _08(array, rez=-1):
    """В каждой клетке массива указана максимальная длина
    следующего прыжка. Функция возвращает минимальное
    количество прыжков, за которое можно допрыгать до конца линии"""
    counter = []
    if len(array) > 1:
        for i in range(1, array[0] + 1):
            try:
                counter.append(_08(array[i:], rez + 1))
            except:
                pass
    else:
        return rez + 1
    return min(counter)


def _09():
    """Функция находит площадь самого большого острова и количество островов."""
    array = ((0, 0, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 1, 0, 0, 0), (0, 0, 0, 1, 1, 1, 0, 0), (1, 0, 0, 1, 0, 0, 0, 0),
             (0, 1, 1, 0, 0, 1, 0, 0), (0, 1, 0, 0, 0, 1, 1, 0), (0, 0, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 1, 0, 0, 0))
    # [[randint(0, 1) for _ in range(n)] for _ in range(n)]
    for i in array:
        print(i)

    def diffusion(point):
        if point not in checked and 0 <= point[0] < len(array) and 0 <= point[1] < len(array):
            checked.append(point)
            if array[point[0]][point[1]] == 1:
                pts = [diffusion((point[0] + 1, point[1])), diffusion((point[0] - 1, point[1])),
                       diffusion((point[0], point[1] + 1)), diffusion((point[0], point[1] - 1))]
                result = [point]
                for q in pts:
                    if q is not None:
                        for w in q:
                            if w is not None:
                                result.append(w)
                return result

    checked = []
    islands = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (i, j) not in checked:
                if array[i][j] == 0:
                    checked.append((i, j))
                else:
                    islands.append(diffusion((i, j)))

    areas = []
    for i in islands:
        areas.append(len(i))
    print("islands: ", len(islands), "\nmax area: ", max(areas))


def _10(array):
    result_global = 0
    for i in range(max(array)):
        started = False
        j = 0
        result_local = 0
        while j < len(array):
            if not started and array[j] <= i:
                pass
            elif array[j] > i:
                started = True
            elif started and array[j] <= i:
                result_local += 1
            j += 1
        result_global += result_local
    for i in range(max(array)):
        started = True
        j = len(array) - 1
        result_local = 0
        while j >= 0:
            if not started and array[j] <= i:
                pass
            elif array[j] > i:
                started = False
            elif started and array[j] <= i:
                result_local += 1
            j -= 1
        result_global -= result_local
    return result_global


def _11():
    """Функция переводит полученое выражение в обратную польскую нотацию
    и вычисляет его значение"""
    PRIORITY = {1: ['+', '-'], 2: ['*', '/']}
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    def priority(value):
        for k, v in PRIORITY.items():
            if value in v:
                return k
        return -1

    def to_pol_notation(expr):
        result = []
        stack = []
        for element in expr:
            if element not in '+-*/':
                result.append(element)
            else:
                last = None if not stack else stack[-1]
                while priority(last) >= priority(element):
                    result.append(stack.pop())
                    last = None if not stack else stack[-1]
                stack.append(element)
        for e in reversed(stack):
            result.append(e)
        return ''.join(result)

    def calc_pol_notation(srt):
        stack = []
        lst = list(srt)
        for i in srt:
            if i.isdigit():
                stack.append(i)
                lst.remove(i)
            else:
                cnt1, cnt2 = stack.pop(), stack.pop()
                stack.append(OPERATORS[i](int(cnt2), int(cnt1)))
                lst.remove(i)
        return stack.pop()

    print(calc_pol_notation(to_pol_notation(input())))


def _12(a1=(10, 9), a2=(1, 4), b1=(4, 7), b2=(13, 2)):
    """Функция получает на вход 4 точки -
    координаты противоболожных вершин двух прямоугольников.
    Функция находит площадь площадь прямоугольника,
    который является результатом пересичения двух первых.
    ! Продразумевается, что прямоугольники,
    координаты которых получает функция, пересекаются."""
    c1 = []
    c2 = []
    # x stabilization
    if a1[0] > a2[0]:
        a1, a2 = a2, a1
    if b1[0] > b2[0]:
        b1, b2 = b2, b1
    # x
    if a1[0] < b1[0] < a2[0] < b2[0]:
        c1.append(b1[0])
        c2.append(a2[0])
    else:
        c1.append(a1[0])
        c2.append(b2[0])
    # y stabilization
    if a1[1] > a2[1]:
        a1, a2 = a2, a1
    if b1[1] > b2[1]:
        b1, b2 = b2, b1
    # y
    if a1[1] < b1[1] < a2[1] < b2[1]:
        c1.append(b1[1])
        c2.append(a2[1])
    else:
        c1.append(a1[1])
        c2.append(b2[1])
    # area
    return abs((c1[0] - c2[0]) * (c1[1] - c2[1]))


def start():
    # print(_01(int(input("Enter k: ")), int(input("Enter n: "))))
    # print(_02(int(input("Enter k: ")), int(input("Enter N: "))))
    # print(_03(int(input("Enter k: ")), int(input("Enter n: ")), -5, 5))
    # print('Всего украдено на:', _04_a(), "\n\n----------------\n")
    # _04_b()
    # print(_05())
    # print(_06())
    # print(_07(8))
    # print(_08([2, 3, 1, 1, 4]))
    # _09()
    # print(_10([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # _11()
    print(_12())
    pass


start()
