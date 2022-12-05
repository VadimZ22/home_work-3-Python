# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     *Пример:*
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10


n = int(input("enter a number: "))
bin_num = []
process = True
while process:
    if n // 2 == 0: process = False
    bin_num.append(n % 2)
    n = n//2

bin_num.reverse()
for i in bin_num:
    print(i, end = '')
