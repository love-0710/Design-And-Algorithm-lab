p=input("Enter Words seperated by commas: ")
p=p.split(",")
m={}
for i in p:
        q=i
        q="".join(sorted(q))
        if q in m:
                m[q].append(i)
        else:
                m[q]=[i]
for i in m:
        if len(m[i])!=1:
                print(m[i])

