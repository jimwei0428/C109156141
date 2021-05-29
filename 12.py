x=input("輸入一整數序列為:").split()
l=[]
for i in range(len(x)):
    a=x.count(x[i])
    l.append(a)
y=max(l)
z=l.index(y)
if y>len(x)/2:
    print("過半元素為:",x[z])
else:
    print("過半元素為NO:")
