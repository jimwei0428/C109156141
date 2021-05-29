a=input("").split(",")
a.sort()
b=""
for i in a:
    b+=i
print(int(b[::-1])-int(b))