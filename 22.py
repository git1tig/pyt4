# ; Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# ;  все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# ;   m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


def fillList(arrlength, arrname):
    myList = []
    for i in range(arrlength):
        myList.append(int(input(f'Введите элемент {i+1} {arrname} набора ')))
    return myList

a = int(input('Введите размер первого набора:'))
list1 = fillList(a, 'первого')

b = int(input('Введите размер второго набора:'))
list2 = fillList(b, 'второго')
list3 =[]
print (list1)
print (list2)

for i in range (a):
    for j in range (b):
        if list1[i] == list2[j]:
            list3.append(list1[i])
list3.sort()
print (list3)







