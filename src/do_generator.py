# -*- coding: utf-8 -*-

def triangles(nMax):
    L= []
    n = 1
    while n <= nMax:
        if n == 1:
            L.append(1)
        else:
            for i in range(0,n):
                if i == 0:
                    continue
                if i == n-1:
                    L.append(1)
                else:
                    L[i] = L1[i-1] + L1[i]
        n+=1
        L1 =L.copy()
        yield (L)
    return "done"

f = triangles(10)
print(next(f))