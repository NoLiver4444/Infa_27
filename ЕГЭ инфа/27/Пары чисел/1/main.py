#Открываем файл
with open("27-B_2.txt", "r") as a:
    b = a.readlines()
    n = int(b[0])
    b = list(map(int, b[1:]))

#Находим максимальные числа кратные 7, 2 и 14
m7 = max(filter(lambda x: x % 7 == 0 and x % 2 != 0, b))
m2 = max(filter(lambda x: x % 7 != 0 and x % 2 == 0, b))
m14 = max(filter(lambda x: x % 14 == 0, b))
#Максимальное число в последовательности, не совпадающее с m14 по индексу
#я выводил m и смотрел на количество максимальных чисел и совпадение с m14
m = sorted(b)

print(max(m2 * m7, m14 * m[-1]))