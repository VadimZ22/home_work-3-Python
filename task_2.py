# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#     *Пример:*
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

def Get_List():
    lst = [float(i) for i in input("enter elements: ").split()]
    return lst

def Get_Difference(lst):
    min = 1
    max = 0
    for i in lst:
        temp = abs(i % 1)
        if temp < min: min = temp
        if temp > max: max = temp
    #print(min, max)
    return round(max - min, 2)

print(Get_Difference(Get_List()))