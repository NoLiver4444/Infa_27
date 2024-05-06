# Открываем файл
with open("27991_B.txt", "r") as a:
    b = a.readlines()
    n = int(b[0])
    b = list(map(int, b[1:]))

# Чтобы разность была чёт оба числа должны быть н/чёт или чёт
# И одно число должно быть кратно 17
####Для файла A max_17_ch будет пустым => оно равно 0
max_17_ch = max(filter(lambda x: x % 2 == 0 and x % 17 == 0, b))
max_ch = max(filter(lambda x: x % 2 == 0 and x % 17 != 0, b))

max_17_nch = max(filter(lambda x: x % 2 != 0 and x % 17 == 0, b))
max_nch = max(filter(lambda x: x % 2 != 0 and x % 17 != 0, b))

# Находим максимальную пару
print(max([max_17_ch, max_ch], [max_17_nch, max_nch]))