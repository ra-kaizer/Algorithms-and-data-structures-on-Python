# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# Примечания:
# 1. В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.

count = 0


def recur_method(n, b):
    global count
    if n == 0:
        return f"Было введено {count} цифр {b}"
    m = int(input(f"Введите число: "))
    while m > 0:
        if m % 10 == b:
            count += 1
        m = m // 10
    return recur_method(n - 1, b)


try:
    N = int(input(f"Сколько будет введено чисел: "))
    B = int(input(f"Какую цифру искать: "))
    print(recur_method(N, B))
except ValueError:
    print("Вы ввели строку! Начните заново!")
