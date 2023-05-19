k=input("Enter a word: ")
p=list(k)
i=0
while i<len(p)-1:
        if i%2==1:
                p[i+1],p[i]=p[i],p[i+1]
        i+=1
p="".join(p)
print(p)

