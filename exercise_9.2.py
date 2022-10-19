def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

fin = open('words.txt')
count = 0
number_of_words = 113809

for line in fin:
    word = line.strip()
    if has_no_e(word) == True:
        count += 1
        print(word)

print(count / number_of_words * 100, '%')
