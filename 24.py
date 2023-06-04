# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику... Лучше б не выращивали!

import random

# получаем любой индекс от массива со смещением. Разве что большие отрицательные не поймёт..но тут и не надо же? :)
def getShifted(myarr, ind):
    if ind < 0:
        return myarr[len(myarr)+ind]
    if len(myarr) > ind:
        return myarr[ind]
    return myarr[ind % len(myarr)]


col = int(input('Введи количество кустов на круглой грядке:'))

Gradka = [random.randint(5, 10) for i in range(col)]
maxberry = 0
maxindex = 0
print(f' Что выросло, то выросло: {Gradka}')

for i in range(col):
    if (Gradka[i] + getShifted(Gradka, i+1) + getShifted(Gradka, i-1)) > maxberry:
        maxberry = Gradka[i] + getShifted(Gradka, i+1) + getShifted(Gradka, i-1)
        maxindex = i

print(f'Максимум c этой грядки робот снимет {maxberry} ягод c {maxindex+1} кучки. Больше никак!')
