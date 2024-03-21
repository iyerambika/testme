given_str = 'Geekforgeeks'
 
# given input string
even_characters = ""
if len(given_str) <= 1:
    print(given_str)
else:
    for i in range(len(given_str)):
        if i % 2 != 0:
            even_characters += given_str[i]
    print(even_characters)        



