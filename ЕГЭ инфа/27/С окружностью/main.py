#Приложу фото......
with open("1_27_A (2).txt", "r") as a:
    b = a.readlines()
    n = int(b[0]) - 1
    b = list(map(int, b[1:]))

s = 0
k = 0
r = 0
r_k = 0
l = 0
l_k = 0
N = b[0]

for i in range(1, n // 2 + 1):
    k = i
    s += b[i] * k + b[i - (2 * k)] * k
    r += b[i]
    r_k += b[i] * k
    l_k += b[i - (2 * k)] * k
    l += b[i - (2 * k)]

k = k + 1
s += b[n // 2 + 1] * k
m = b[n // 2 + 1]
m_k = b[n // 2 + 1] * k
mi = s

for i in range(1, n + 1):
    s = (r_k - r) + (m_k - m) + l_k + l + N
    l_k = l_k + l + N
    r_k = (r_k - r) + (m_k - m)
    N_p = N
    N = b[i]
    r = r - N + m
    index = n // 2 + i + 1
    if index > n:
        index = index - n - 1
    m = b[index]
    m_k = m * k
    l_k = l_k - m_k
    l = l - m + N_p
    mi = min(mi, s)

print(mi)