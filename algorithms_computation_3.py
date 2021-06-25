def _01(n):
    if n == 1:
        return 1
    elif n < 1:
        return 0
    array = range(1, int(n) + 1)
    size = len(array)
    left = 0
    right = size - 1
    while left <= right:
        m = left + (right - left) // 2
        if ((array[m]) ** 2) <= n < ((array[m + 1]) ** 2):
            return array[m]
        elif ((array[m]) ** 2) < n:
            left = m + 1
        elif ((array[m]) ** 2) > n:
            right = m - 1
    return -1


def _02(array, t):
    sep = binary_offset_search(array)
    result_l = binary_search(array[:sep], t)
    result_r = binary_search(array[sep:], t)
    if result_r == -1:
        return result_l
    return max(result_l, result_r + sep)


def _03(array):
    size = len(array)
    if array[0] >= array[1]:
        return array[0]
    elif array[size - 1] >= array[size - 2]:
        return array[size - 1]
    left = 0
    right = size - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid - 1] <= array[mid] >= array[mid + 1]:
            return array[mid]
        elif array[mid - 1] >= array[mid]:
            right = mid
        elif array[mid] <= array[mid + 1]:
            left = mid
        else:
            print("error")


def _04(array):
    return array[binary_offset_search(array)]


def _05(array, t):
    return [binary_search_leftmost(array, t), binary_search_rightmost(array, t)]


def _06(array, k, x):
    counter = 0
    result = []
    for i in range(x - 1, x - k - 1, -1):
        if i >= 0:
            result.insert(0, array[i])
            counter += 1
        else:
            break
    for i in range(x + 1, x + k - counter + 1):
        try:
            result.append(array[i])
        except:
            break
    return result


def _07(x, n):
    result = x
    if n > 0:
        for i in range(n - 1):
            result *= x
    elif n == 0:
        result = 1
    elif n == -1:
        result = 1 / x
    else:
        result = 1
        for i in range(-n - 1):
            result /= x
    return result


def start():
    print(_01(64))
    print(_02([4, 5, 6, 7, 0, 1, 2], 0))
    print(_03([1, 2, 1, 3, 5, 6, 4]))
    print(_04([4, 5, 6, 7, 0, 1, 2]))
    print(_05([5, 7, 7, 8, 8, 10], 8))
    print(_06([1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 5))
    print(_07(2, -2))


# функции, которые используются в работе
def binary_offset_search(array):
    size = len(array)
    left = 0
    right = size - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] > array[mid + 1]:
            return mid + 1
        elif array[mid] > array[right]:
            left = mid
        else:
            right = mid + 1


def binary_search(array, t):
    size = len(array)
    left = 0
    right = size - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] < t:
            left = mid + 1
        elif array[mid] > t:
            right = mid - 1
        else:
            return mid
    return -1


def binary_search_leftmost(array, t):
    size = len(array)
    left = 0
    right = size
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < t:
            left = mid + 1
        else:
            right = mid
    if array[left] == t:
        return left
    else:
        return -1


def binary_search_rightmost(array, t):
    size = len(array)
    left = 0
    right = size
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] <= t:
            left = mid + 1
        else:
            right = mid
    if array[left - 1] == t:
        return left - 1
    else:
        return -1


start()
