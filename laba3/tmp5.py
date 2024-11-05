x1, x2, x3 = 100000, 10000, 1000
m = 9999999999999
for i in range(0, 7692):
    for j in range(0, 7692):
        for k in range(0, 7692):
            t1 , t2, t3 = i/10000000, j/10000000, k/10000000
            if (20*t1 + 15*t2 + 10*t3) >= 1 and (16*t1 + 12*t2 + 14*t3) >= 1 and (13*t1 + 18*t2 + 15*t3) >= 1:
                if t1 + t2 + t3 < m:
                    x1 , x2 ,x3 = t1, t2, t3
                    m = t1 + t2+ t3
                    print(x1, x2, x3, m)
print(x1, x2, x3, m)
