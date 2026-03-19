h, m, s = map(int, input("").split())
t = int(input(""))

if (s+t>59):
    m += (s+t) // 60
    s = (s+t) % 60
    if (m > 59):
        h += m // 60
        m = m % 60
        if (h>23):
            h = h % 24
else: s += t
print(h, m, s)