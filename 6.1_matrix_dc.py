import numpy as np
import time
def split(matrix):
        r,c=matrix.shape
        r2,c2=r//2,c//2
        return matrix[:r2,:c2],matrix[:r2,c2:],matrix[r2:,:c2],matrix[r2:,c2:]
def divide(x,y):
        if x.size==1 or y.size==1:
                return x*y
        n=x.shape[0]
        if n%2==1:
                x=np.pad(x,(0,1),mode='constant')
                y=np.pad(y,(0,1),mode='constant')
        a,b,c,d=split(x)
        e,f,g,h=split(y)
        p1=divide(a,e)
        p2=divide(b,g)
        p3=divide(a,f)
        p4=divide(b,h)
        p5=divide(c,e)
        p6=divide(d,g)
        p7=divide(c,f)
        p8=divide(d,h)
        c11=p1+p2
        c12=p3+p4
        c21=p5+p6
        c22=p7+p8
        c=np.vstack((np.hstack((c11,c12)),np.hstack((c21,c22))))
        return c
#driver code
a=[[2,2,3],[4,1,4],[7,0,2]]
b=[[1,0,0], [0,1,0], [0,0,1]]
t1=time.time()
print(divide(np.array(a),np.array(b)))
print(time.time()-t1)

