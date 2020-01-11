#coding:utf-8

def findMinAndMax(n):
    if type(n) != list:
        return "%s不是列表"%n
    else:
        if n == []:
            return (None,None)
        else:
            for i in n:
                if type(i) == int:
                    continue
                else:
                    return "%s不是数字"%i
            nMax = n[0]
            nMin = n[0]
            for j in range(0,len(n)):
                if  nMax >= n[j]:
                    continue
                else:
                    nMax = n[j]

            for j in range(0, len(n)):
                if nMin <= n[j]:
                    continue
                else:
                    nMin = n[j]
            return (nMin,nMax)



print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7,1]))
print(findMinAndMax([7,1,3,9,10,0]))