# -*- coding: utf-8 -*-
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# def by_name(L):
#     L1 = sorted(L,key=str)
#     print(L1)
# def by_score(L):
#     L1 = sorted(L,key = (L[i][1] for i  in L),reverse=True)
#     print(L1)
# by_name(L)
# by_score(L)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))