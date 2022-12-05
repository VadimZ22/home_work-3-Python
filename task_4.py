# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     *Пример:*
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("enter a number: "))
fibo_list = [0]
first = 0
current = 1
for i in range(1, num+1):
    next = first + current
    fibo_list.insert(i, current)
    first = current
    current = next
first = 0
current = 1
for i in range(1, num+1):
    next = first - current
    fibo_list.insert(0, current)
    first = current
    current = next

print(fibo_list)