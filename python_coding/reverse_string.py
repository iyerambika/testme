stra = "Hello"
# print(str[::-1])
# reversed_str = "".join(reversed(str))
# print(reversed_str)
str1 = ""
length_str = len(stra)
i = len(stra) - 1

if length_str == 0:
    print(stra)
else:
    while i >= 0:
        str1 += str[i]
        i -= 1
    print(str1)




    