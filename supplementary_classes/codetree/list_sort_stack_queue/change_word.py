word1 = input()
word2 = input()

dic_word1, dic_word2 = {}, {}
for char in word1:
    dic_word1[char] = dic_word1.get(char, 0) + 1

for char in word2:
    dic_word2[char] = dic_word2.get(char, 0) + 1

if dic_word1 == dic_word2:
    print("Yes")
else:
    print("No")