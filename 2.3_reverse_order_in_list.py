a=[1,"Hi",23,False,67,8.09]
for i in range(0,len(a)//2):
        a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
print(a)

