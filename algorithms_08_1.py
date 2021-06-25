#щоб опорним елементом в процедурі Partition обирався останній елемент поточного масиву
def partition_1(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort_1(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition_1(arr, low, high)
        quickSort_1(arr, low, pi - 1)
        quickSort_1(arr, pi + 1, high)


#щоб опорним елементом в процедурі Partition обирався перший елементпоточного масиву
def partition_2(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort_2(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        arr[low], arr[high] = arr[high], arr[high]
        pi = partition_2(arr, low, high)
        quickSort_2(arr, low, pi - 1)
        quickSort_2(arr, pi + 1, high)


#щоб опорним елементом в процедурі Partition обирається медіана серед трьох елементів поточного масиву: першого, останнього та середнього
def partition_3(arr, low, high):
    i = (low - 1)
    if arr[high] >= arr[(high + low) // 2] >= arr[low] or arr[high] <= arr[(high + low) // 2] <= arr[low]:
        pivot = arr[(high + low) // 2]
    elif arr[(high + low) // 2] >= arr[high] >= arr[low] or arr[(high + low) // 2] <= arr[high] <= arr[low]:
        pivot = arr[high]
    else:
        pivot = arr[low]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort_3(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition_3(arr, low, high)
        quickSort_3(arr, low, pi - 1)
        quickSort_3(arr, pi + 1, high)


array = [3, 7, 1, 9, 5]
quickSort_1(array, 0, len(array) - 1)
print(array)
array = [3, 7, 1, 9, 5]
quickSort_2(array, 0, len(array) - 1)
print(array)
array = [3, 7, 1, 9, 5]
quickSort_3(array, 0, len(array) - 1)
print(array)
