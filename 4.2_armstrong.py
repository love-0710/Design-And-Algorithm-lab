print("Armstrong nos between 1 and 1000 are:")
for j in range(1,1000):
        s=0
        l=len(str(j))
        for i in str(j):
                s+=int(i)**l
        if s==j:
                print(j)

