str ="hello"
n = 1
ran = len(str)
if n > len(str):
    print(f" Index is  Out of range. string is {str}")
elif len(str) == 0:
    print(f" String is empty. string is {str}")
else:
    str2 = ""
    for i in range(len(str)):
        if i != n:
            str2 += str[i]
    print(str2)       

 