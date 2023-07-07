import random
lst1 = []
lst2 = []
i = 1
while i <=10:
    lst1.append(random.randint(1,10))
    lst2.append(random.randint(1,10))
    i += 1
set1 = set(lst1)
set2 = set(lst2)
set_common = set1.intersection(set2)
lst_common = list(set_common)



