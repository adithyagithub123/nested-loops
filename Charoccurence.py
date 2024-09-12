word = input("Enter a word: ")
char = input("Enter a character: ")

i = 0
count = 0

while (i<len(word)):
    if (word[i] == char):
        count = count + 1
    i = i + 1

print("Total number of occurence is : ", count)

