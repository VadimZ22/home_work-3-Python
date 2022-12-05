# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

def Get_List():
    lst = [int(i) for i in input("enter elements: ").split()]
    return lst

def Product_of_Pairs(lst):
    result_lst = []
    if len(lst) % 2 == 0:
        len_res_lst = len(lst) / 2
    else: len_res_lst = len(lst) / 2 + 1
    for i in range(int(len_res_lst)):
        result_lst.append(lst[i] * lst[-(i+1)])
    return result_lst

lst = Get_List()
print(Product_of_Pairs(lst))



