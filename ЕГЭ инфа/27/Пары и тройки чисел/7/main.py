#Открываю файл
with open("inf_22_10_20_27b.txt", "r") as a:
    b = a.readlines()
    n = int(b[0])
    b = list(map(lambda x: sorted(list(map(int, x.split()))), b[1:]))

#d1 и d2 массивы с остатком отделения 1 и 2
s = 0
d1 = []
d2 = []

for i in b:
    # Суммирую минимальные элементы и нахожу замены
    s = s + i[0]
    q = i[1] - i[0]

    if q % 3 == 1:
        d1.append(q)
    elif q % 3 == 2:
        d2.append(q)

#Сортирую массивы с заменами
d1 = sorted(d1)
d2 = sorted(d2)

if s % 3 == 0:
    print(s)
else:
    #Если остаток от деления на 3 равен 1,
    #то чтобы получить 0 мы можем вычесть прибавить из d2 или 2 минимальных из d1
    #Для остатка 2 d1[0], d2[0] d2[1]
    if s % 3 == 1:
        print(min(s + d2[0], s + d1[0] + d1[1]))
    else:
        print(min(s + d1[0], s + d2[0] + d2[1]))