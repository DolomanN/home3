# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = input ("введите число: ")

def binary(n):
    a = ''
    while int(n) > 0:
        a = str(int(n) % 2) + a
        n = int(n)//2
    return a
print (f'десятичное чило {n} при переводе в двоичну систему примет вид {binary(n)}')