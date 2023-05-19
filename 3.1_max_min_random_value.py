import random

def list_info(my_list):
        return(len(my_list),min(my_list),max(my_list))

my_list=random.sample(range(1,100),10)
print(list_info(my_list))


