def start():
    file = open("input_1000_5.txt")
    lines = file.read().split("\n")
    lst = []
    for i in lines:
        lst_inner = i.split(" ")
        lst.append(lst_inner)
    file.close()
    print(lst)
    for i in range(len(lst)):
        print(f"Користувач {i + 1}: ", merge_count_inversion(lst[i])[1])


def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int(len(lst) / 2)
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)


def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count


start()
