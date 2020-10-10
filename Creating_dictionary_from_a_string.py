sentence = "the dog chased the rabbit into the forest but the rabbit was too quick"

print(sentence)
word_counts={}

for i in sentence:
    if i not in word_counts:
        word_counts[i]=0
    word_counts[i]=word_counts[i]+1

print(word_counts)
del word_counts[' ']

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 
                 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1,
                 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

tot=0
for i in word_counts:
    if i in word_counts:
        tot = tot + word_counts[i] * letter_values[i]
print(tot)