vowel = ['a','e','i','o','u']
strA = "Ambika"
count = 0
for element in strA.lower():
    if element in vowel:
        count += 1
print(count)        