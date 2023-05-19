import random
class Item:
        def __init__(self,i,value,weight):
                self.name=i
                self.value=value
                self.weight=weight
def knapsack(arr,W):
        arr.sort(key=lambda a: a.value/a.weight,reverse=True)
        profit=0
        selected=[]
        print(f"Total Weight {W}")
        for item in arr:
                if(W==0):
                        break
                if(item.weight<=W):
                        profit+=item.value
                        W-=item.weight
                        selected.append((item.name,item.weight,item.value))
                else:
                        profit+=item.value*W/item.weight
                        selected.append((item.name,W,item.value*W/item.weight))
                        W=0
        print(f"Profit earned={profit}")
        print("Selected Items:")
        print("Item\tWeight Selected\tValue Earned")
        for i in selected:
                print(f"{i[0]}\t{i[1]}\t\t{i[2]}")

if __name__=='__main__':
        items=[]
        print("All Items")
        print("Item\tWeight\tValue")
        value=[1,3,5,4,1,3,2]
        weight=[5,10,15,7,8,9,4]
        for i in range(len(value)):
                items.append(Item(f"Item {i+1}",weight[i],value[i]))
                print(f"{items[i].name}\t{items[i].weight}\t{items[i].value}")
        print()
        knapsack(items,15)




