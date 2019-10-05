# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s,str) ]
print(L2)

d = [{ 'Adam': 95, 'Lisa': 85, 'Bart': 59 },{ 'Lancer': 95, 'Acher': 85, 'Altolia': 59 }]
def generate_tr(name, score):
    if score<60:
       return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = []
for i in range(len(d)):
    tds.append([generate_tr(name,score) for name, score in d[i].items()])
print( '<table border="1">')
print('<tr><th>Name</th><th>Score</th><tr>')
for i in range(len(tds)):
    print('\n'.join(tds[i]))
print( '</table>')
