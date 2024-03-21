# str = "Hello"
# curr_char = "p"
# new_char = "s"

# # Check if curr_char exists in the string before replacing
# if curr_char in str:
#     new_str = str.replace(curr_char, new_char)
# else:
#     new_str = str

# print(new_str)

s = "Hello"
new_s = ""

curr_char = "l"
new_char = "s"

for char in s:
    if char == curr_char:
        new_s += new_char
    else:
        new_s += char

print(new_s)