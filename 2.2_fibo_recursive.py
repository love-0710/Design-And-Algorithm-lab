n=int(input("Enter n:"))

def fib(a,b,i):
        if i>=n:
                return
        else:
                print(a+b)
                i+=1
                fib(b,a+b,i)
fib(1,0,0)









