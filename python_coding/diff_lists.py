lstA = [1, 2, 3, 4]
lstB = [1,2]
new_lst = []
for i in lstA:
    if i not in lstB:
        new_lst.append(i)
print(new_lst)
