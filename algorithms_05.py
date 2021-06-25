def error():
    print("\033[1m\033[31mPlease, input correct values\033[0m")


def line(*kargs):
    result = ""
    for i in kargs:
        result += f"\t{i}"
    print(result)


def linearSearch(n, k):
    print("linear Search")
    for i in k:
        result = "NO"
        if i in n:
            result = "YES"
        line(i, result)


def binarySearchInitialize(n, k):
    print("binary Search")
    for i in range(len(n)):
        n[i] = int(n[i])
    for i in k:
        i = int(i)
        result = "NO"
        if binarySearch(sorted(n), i):
            result = "YES"
        line(i, result)


def binarySearch(n, elem):
    first = 0
    last = len(n) - 1
    result = False
    while first <= last and not result:
        middle = (first + last) // 2
        if n[middle] == elem:
            result = True
        else:
            if elem < n[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return result


def start():
    try:
        n_k = input("enter N and K separated by a space: ").split(" ")
        N, K = int(n_k[0]), int(n_k[1])
        if N <= 0 or K > 100000:
            error()
            return
        n = input(f"enter {N} numbers separated by a space: ").split(" ")
        if len(n) != N:
            error()
            return
        k = input(f"enter {K} numbers separated by a space: ").split(" ")
        if len(k) != K:
            error()
            return
        for i in n + k:
            if 10 ** 9 < int(i) or int(i) < -(10 ** 9):
                error()
                return
        linearSearch(n, k)
        binarySearchInitialize(n, k)
    except:
        error()


if __name__ == "__main__":
    while True:
        start()
