a=input("輸入通話費型式及通話時間:").split(",")
b=int(a[0])
c=int(a[1])
if b==186:
    if c*0.09<=b:
        print("通話費為:"+str(int(round(c*0.09*0.9,0))))
    elif c*0.09>b:
        print("通話費為:"+str(int(round(c*0.09*0.8,0))))
if b==386:
    if c*0.08<=b:
        print("通話費為:"+str(int(round(c*0.08*0.8,0))))
    elif c*0.08>b:
        print("通話費為:"+str(int(round(c*0.08*0.7,0))))
if b==586:
    if c*0.07<=b:
        print("通話費為:"+str(int(round(c*0.07*0.7,0))))
    elif c*0.07>b:
        print("通話費為:"+str(int(round(c*0.07*0.6,0))))
if b==986:
    if c*0.06<=b:
        print("通話費為:"+str(int(round(c*0.06*0.6,0))))
    elif c*0.06>b:
        print("通話費為:"+str(int(round(c*0.06*0.5,0))))
else:
    print("沒有此通話費型式")