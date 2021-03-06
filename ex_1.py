# https://drive.google.com/file/d/1-4pe3U8NdxGBvw9GILLFlvuDNrlvx6P4/view?usp=sharing
# ссылка на схемы(алгоритмы)

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = input("Введите трехзначное число: ")
n = int(n)

d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100

print("Сумма цифр числа:", d1 + d2 + d3)
print("Произведение цифр числа:", d1 * d2 * d3)

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
print("%d = %s" % (a, bin(a)))
b = 6
print("%d = %s" % (b, bin(b)))

print("%d И %d = %d (%s)" % (a, b, a & b, bin(a & b)))
print("%d ИЛИ %d = %d (%s)" % (a, b, a | b, bin(a | b)))
print("%d Исключительное ИЛИ %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
print("%d Побитовый сдвиг влево 2 = %d (%s)" % (a, a << 2, bin(a << 2)))
print("%d Побитовый сдвиг вправо 2 = %d (%s)" % (a, a >> 2, bin(a >> 2)))

# 5.Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
a = ord(input('1-я буква: '))
b = ord(input('2-я буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print('Позиции: %d и %d' % (a, b))
print('Между буквами букв:', abs(a - b) - 1)

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input('Номер буквы в алфавите: '))
n = ord('a') + n - 1
print('Это буква', chr(n))

# 8. Определить, является ли год, который ввел пользователь, високосным или не високосным.
year = int(input())
if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")
# тест год 3008

# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
n = a + b + c
print(n - max(a, b, c) - min(a, b, c))
