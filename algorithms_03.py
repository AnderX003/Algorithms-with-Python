def printResult():
    print("Repetitions:")
    for i in result:
        print("\tad + bc = ", i, "\tRepetitions: ", result[i])


def multiply(X, Y):
    if len(str(X)) == 1 and len(str(Y)) == 1:
        return X * Y
    n = max(len(str(X)), len(str(Y)))

    a = X // 10 ** int(n / 2)
    b = X % 10 ** int(n / 2)
    c = Y // 10 ** int(n / 2)
    d = Y % 10 ** int(n / 2)

    ac = multiply(a, c)
    bd = multiply(b, d)
    ad_plus_bc = multiply((a + b), (c + d)) - ac - bd

    if ad_plus_bc in result:
        result[ad_plus_bc] += 1
    else:
        result[ad_plus_bc] = 1
    return ac * 10 ** n + ad_plus_bc * 10 ** int(n / 2) + bd


global result
if __name__ == '__main__':
    result = {}
    while True:
        try:
            print("Result: ", multiply(int(input("\ninput x: ")), int(input("input y: "))))
            printResult()
        except:
            print("\033[1m\033[31mPlease, input correct values\033[0m")
