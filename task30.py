a1 = int (input ('Введите число: '))
d = int (input ('Введите число - разность: '))
n = int (input ('Введите количество элементов: '))
for i in range (1, n + 1):
    print (a1 + (i - 1) * d)
