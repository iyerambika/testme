lenofname = input()
if not all(char.isalpha() or char.isspace() for char in lenofname):
  raise ValueError("Input should only contain alphabetic characters")

print(len(lenofname))