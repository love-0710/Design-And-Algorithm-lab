import itertools
p=input("Enter a word: ")
n=list(itertools.permutations(p)) #without repetition
#n=list(itertools.product(p,repeat=len(p))) #with repetition
for i in n:
        print("".join(i))


