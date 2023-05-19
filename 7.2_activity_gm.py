import random
class Activity:
        def __init__(self,i,start,finish):
                self.name=i
                self.start=start
                self.finish=finish
def knapsack(arr):
        arr.sort(key=lambda a:a.finish)
        selected=[None]*arr[-1].finish
        for act in arr:
                f=0
                for i in range(act.start-1,act.finish):
                        if(selected[i]!=None):
                                f=1
                                break
                if f==0:
                        for i in range(act.start-1,act.finish):
                                selected[i]=act
        m=[]
        print("\nSelected Activities")
        print("Activity\tStart\tFinish")
        for i in selected:
                if i not in m:
                        m.append(i)
                        print(f"{i.name}\t\t{i.start}\t{i.finish}")


if __name__=='__main__':
        items=[]
        print("All Activities")
        print("Activity\tStart\tFinish")
        start=[5,1,3,0,5,8]
        finish=[9,2,4,6,7,9]
        for i in range(len(start)):
                #start=random.randint(1,10)
                items.append(Activity(f"Item {i+1}",start[i],finish[i]))
                print(f"{items[i].name}\t\t{items[i].start}\t{items[i].finish}")
        print()
        knapsack(items)


