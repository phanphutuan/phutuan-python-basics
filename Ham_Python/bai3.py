def kiem_tra_so_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

print(kiem_tra_so_fibonacci(14))