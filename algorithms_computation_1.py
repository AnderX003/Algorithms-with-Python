def A(n, i=1):
    print(i)
    if i == n:
        return
    A(n, i + 1)


def B(a, b):
    print(a)
    if a == b:
        return
    elif a < b:
        B(a + 1, b)
    else:
        B(a - 1, b)


def C(m, n):
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return C(m - 1, 1)
    elif m > 0 and n > 0:
        return C(m - 1, C(m, n - 1))


def D(n):
    if D_1(n):
        print("YES")
    else:
        print("NO")


def D_1(n):
    if n == 1:
        return True
    elif 1 < n < 2:
        return False
    else:
        return D_1(n / 2)


def E(n):
    i = n % 10
    n //= 10
    if n == 0:
        return i
    else:
        return i + E(n)


def F(n):
    print(n % 10)
    if n >= 10:
        F(n // 10)


def G(n):
    if n >= 10:
        G(n // 10)
    print(n % 10)


def H(n, i=2):
    if n < 2:
        return False
    elif n == 2:
        return True
    if n % i == 0:
        return False
    elif i < n / 2:
        return H(n, i + 1)
    else:
        return True


def I(n, i=2):
    if i > n / 2:
        print(n)
        return
    if n % i == 0:
        print(i)
        I(n // i, i)
    else:
        I(n, i + 1)


def J(string):
    if len(string) == 1:
        print("YES")
        return
    elif string[0] == string[-1]:
        if len(string) == 2:
            print("YES")
            return
        return J(string[1:-1])
    else:
        print("NO")
        return


def K():
    n = int(input())
    if n == 0:
        return
    if n % 2 == 0:
        K()
        print(n)
    else:
        K()


def L():
    n = int(input())
    if n == 0:
        return
    print(n)
    m = int(input())
    if m != 0:
        L()


def M():
    n = int(input())
    if n == 0:
        return 0
    rez = M()
    if rez == 0 or rez < n:
        return n
    else:
        return rez


def N(s=0, i=0):
    n = int(input())
    if n > 0:
        N(s + n, i + 1)
    elif s > 0 and i > 0:
        print(s / i)


def O(f=0, s=0):
    n = int(input())
    if n == 0:
        print(s)
        return
    if f >= s >= n:
        O(f, s)
    elif f >= n >= s:
        O(f, n)
    else:
        O(n, f)


def P():
    n = int(input())
    if n == 0:
        return
    rez = P()
    if not rez:
        return n, 1
    elif rez[0] > n:
        return rez
    elif rez[0] == n:
        return rez[0], (rez[1] + 1)
    else:
        return n, 1


def Q():
    n = int(input())
    if n == 0:
        m = int(input())
        if m == 0:
            return 0
        elif m == 1:
            return Q() + 1
        else:
            return Q()
    elif n == 1:
        return Q() + 1
    else:
        return Q()


def R(n):
    if n != 1:
        R(n - 1)
    for e in range(1, n + 1):
        print(n, sep="", end=", ")


def S(k, s, i=None, max=None):
    if not max:
        i = 10 ** (k - 1)
        max = 10 ** k - 1
    current_s = 0
    a = i
    for e in range(1, k + 1):
        current_s += a % 10
        a //= 10
    if i == max:
        return 0
    elif s == current_s:
        return S(k, s, i + 1, max) + 1
    else:
        return S(k, s, i + 1, max)


def T(a, b):
    if a > b + 1:
        return 0
    if a == 0 or b == 0:
        return 1
    return T(a, b - 1) + T(a - 1, b - 1)


def U(n, i=0):
    if n != 0:
        return U(n//10, i*10 + n % 10)
    else:
        return i


if __name__ == '__main__':
    A(int(input("n: ")))
    B(int(input("A: ")), int(input("B: ")))
    print(C(int(input("m >= 0: ")), int(input("n >= 0: "))))
    D(int(input("n: ")))
    print(E(int(input("n: "))))
    F(int(input("n: ")))
    G(int(input("n: ")))
    print(H(int(input("n: "))))
    I(int(input("n: ")))
    J(input("string: "))
    K()
    L()
    print(M())
    N()
    O()
    print(P()[1])
    print(Q())
    R(int(input()))
    print(S(int(input()), int(input())))
    print(T(int(input()), int(input())))
    print(U(int(input())))
