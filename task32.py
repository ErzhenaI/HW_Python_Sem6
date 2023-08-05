from random import randint
list_1 = [randint (1, 20) for i in range (1, 20)]
print (list_1)
a = int (input ('Введите первое число: '))
b = int (input ('Введите второе число: '))

list_2 = []
for i in range (len (list_1)):
    if a <= list_1[i] <= b:
        print (i)
