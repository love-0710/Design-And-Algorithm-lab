class Stack:
        def __init__(self,cap):
                self.a=[]
                self.cap=cap
        def push(self):
                if(len(self.a)==self.cap):
                        print("Overflow")
                else:
                        val=input("Enter your value: ")
                        self.a.append(val)
        def pop(self):
                if len(self.a)==0:
                        print("Underflow")
                else:
                        print("Popped Value: ",self.a[-1])
                        return self.a.pop()
        def peek(self):
                if  len(self.a)==0:
                        print("Nothing to display")
                else:
                        print("Peeked Value: ",self.a[-1])
        def display(self):
                print(self.a)

p=Stack(5)
while True:
        try:
                n=int(input("Enter 1 to push, 2 to pop, 3 to peek,4 to display, 5 to quit : "))
                if n==1:
                        p.push()
                elif n==2:
                        p.pop()
                elif n==3:
                        p.peek()
                elif n==4:
                        p.display()
                elif n==5:
                        break
                else:
                        print("Invalid Input. Retry")
        except :
                print("Invalid Input")


