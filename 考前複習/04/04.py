import math
import string
ABC = string.ascii_lowercase


t = input()

f1 = open(t,'r')
file = f1.readlines()

f1.close()

for i in range(len(file)):
    file[i] = file[i].strip()

sentence = []
for i in file:
    i = i.split('-')

    word = ''
    for j in i:
        j = int(math.sqrt(int(j)))
        word += ABC[j-1]
    
    sentence.append(word)

sentence2 = ' '.join(sentence)
print(sentence2)
