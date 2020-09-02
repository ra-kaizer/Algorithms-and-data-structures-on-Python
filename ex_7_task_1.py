"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
from random import randint

int_list = []
for i in range(15):
    int_list.append(randint(-100, 99))
print(int_list)

n = len(int_list)
for j in range(0, n - 1):
    for i in range(0, n - j - 1):
        if int_list[i] < int_list[i + 1]:
            int_list[i], int_list[i + 1] = int_list[i + 1], int_list[i]
    # print(int_list)
print(int_list)

