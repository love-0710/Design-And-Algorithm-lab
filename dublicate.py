import random
p=random.sample(range(1,51),50)
q=random.sample(range(1,51),50)  
p=p+q
m={}
for i in p:
        if i not in m:
                if p.count(i)>1:
                        m[i]=False
for i in range(len(p)):
        if p[i] in m:
                if  m[p[i]]==True:
                        p.pop(i)
                        p.append(-99)
                m[p[i]]=True
print(p)

