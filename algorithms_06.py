import time


def Merge(l, r):
    result = []
    l_index = r_index = 0
    for e in range(len(l) + len(r)):
        if l_index < len(l) and r_index < len(r):
            if l[l_index] <= r[r_index]:
                result.append(l[l_index])
                l_index += 1
            else:
                result.append(r[r_index])
                r_index += 1
        elif l_index == len(l):
            result.append(r[r_index])
            r_index += 1
        elif r_index == len(r):
            result.append(l[l_index])
            l_index += 1
    return result


def MergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_list = MergeSort(array[:mid])
    right_list = MergeSort(array[mid:])
    return Merge(left_list, right_list)


def Start_1():
    array = []
    for i in range(int(input())):
        array.append(int(input()))
    start_time = time.time()
    print("Резульат: ", MergeSort(array), "\nЧас роботи: ", time.time() - start_time)


def Start_2():
    array = input().split(" ")
    for i in range(len(array)):
        array[i] = int(array[i])
    start_time = time.time()
    print("Резульат: ", MergeSort(array), "\nЧас роботи: ", time.time() - start_time)

#Start_1()
#Start_2()
