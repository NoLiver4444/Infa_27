#Открываю файл
with open("27-B_1.txt", "r") as a:
    b = a.readlines()
    n = int(b[0])
    b = list(map(lambda x: list(map(int, x.split())), b[1:]))

#Сортирую все пары по возрастанию
b = list(map(sorted, b))
s = 0
d = 99999999999999

for i in b:
    #Суммирую все максимальные элементы и ищу минимальную замену, которая сможет изменить кратность числа на 5
    #Замена не равняется 0 и не кратна 5
    s = s + i[1]
    q = i[1] - i[0]

    if q < d and q % 5 != 0 and q != 0:
        d = q

#Проверяю кратность суммы максимальных элементов на 5
print(s)
print(s % 5)
#Если s % 5 равняется 0, то скип
#Если не равняется 0, то это ответ

#Дальше вычитаю (т.к. нужени максимум последоватьльности) минимальную замену и проверяю кратность на 5
s = s - d

print(s)
print(s % 5)