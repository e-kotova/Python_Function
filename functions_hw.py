# Задача №306. Минимум 4 чисел
def min4(a, b, c, d):
    m = min(a, b)
    m1 = min(m, c)
    m2 = min(m1, d)
    return m2


a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min4(a, b, c, d))


# Задача №307. Степень
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


a = float(input())
n = int(input())
print(power(a, n))


# Задача №308. Исключающее ИЛИ
def xor(x, y):
    return x != y


x = int(input())
y = int(input())
print(int(xor(x, y)))


# Задача №309. Голосование


# Задача №310. Проверка на простоту_0
def prime(n):
    k = 2
    p = 0
    while k <= pow(n, 0.5) and k > 1:
        if n % k == 0:
            p += 1
        k += 1
    return p == 0


n = int(input())
if prime(n):
    print("prime")
else:
    print("composite")


# Задача №252. Степень для отрицательного показателя
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(power(float(input()), int(input())))


# Задача №311. Быстрое возведение в степень
def power(a, n):
    if n == 0:
        return 1
    res = power(a * a, n // 2)
    if n % 2:
        res *= a
    return res


a = float(input())
n = float(input())
print(power(a, n))


# Задача №312. Числа Фибоначчи
def fibonacci(n):
    a = 1
    if n > 1:
        a = fibonacci(n - 1) + fibonacci(n - 2)
    return a


element = input()
element = int(element)
value = fibonacci(element)
print((value))


# Задача №313. Биномиальные коэффициенты
def C(n, k):
    if k == n or k == 0:
        return 1
    if k != 1:
        return C(n - 1, k) + C(n - 1, k - 1)
    else:
        return n


print(C(int(input()), int(input())))
