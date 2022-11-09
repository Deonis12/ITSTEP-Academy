print('************')
# Task 1
# При заданій цілій кількості n порахуйте n + nn + nnn

def calcul(n,m): # число,яке будемо обчислювати (m - скільки разів це число буде повторюватись(n,nn,nnn)

    # переводимо число в рядок
    str_n = str(n)

    # ініціалізація результату числом та рядком
    sums = n
    sum_str = str(n)

    for i in range(1,m):

        # створення рядка n,nn,nnn
        sum_str = sum_str + str_n

        # перетворюємо назад у ціле число
        sums = sums + int(sum_str)
    return sums
n = 2
m = 3
total = calcul(n,m)
print('Task1:\nAnswer:',total)
print('************')
# Task 2
# Напишіть функцію, яка приймає два числа як параметр і відображає усі парні числа між ними.

def even_num(l): # l - список чисел
    # пустий список
    enum = []
    for n in l:
        # пошук парних чисел
        if n % 2 == 0:
            enum.append(n)
    return enum
print('Task 2:\nAnswer:',even_num([1,2,3,4,5,6,7,8,9]))
