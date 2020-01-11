
f = open("小崇山.txt",'r',encoding='utf8')
# print(f.read())
# print(f.readline(4))
# a = f.readlines()
# print(a)


# for i in a:
#     if a.index(i) == 5:
#         i = "".join([i.strip(),"i like it"])
#     print(i.strip())

# for i in f:
#     print(i.strip())

# data = f.readline()
# data = f.readline()
# print(f.__iter__().__next__())
# for i in range(5):
#     print(f.readline())

for index,line in enumerate(f.readlines()):
    if index==2:
        line=''.join([line.strip(),'end 3'])
    print(line.strip())