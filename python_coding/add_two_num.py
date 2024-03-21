num1 = [2, 7, 11, 15]
num2 = [5, 8, 8]
num3 = []

a = len(num1)
b = len(num2)
c = int(0)

if a>=b or b>=a:
  while True:
    x = num1[c]
    y = num2[c]
    num3.append(x+y)
    c = c+1
    if c == a or c == b:
        break
print(num3)