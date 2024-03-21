def mergeAlternately(word1: str, word2: str) -> str:
    word3 = ""
    # Iterate through the characters of both words
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            word3 += word1[i]
        if i < len(word2):
            word3 += word2[i]
    return word3

word1 = "abc"
word2 = "qr"
print(mergeAlternately(word1, word2))


