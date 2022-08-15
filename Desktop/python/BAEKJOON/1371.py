import sys

alph = [0] * 26

sentence = sys.stdin.read().split()
 
for s in sentence:
    for char in s:
        alph[ord(char)-97] += 1

l = len(alph)
max_ = max(alph)

for idx in range(l):
    if alph[idx] == max_:
        result = chr(idx + 97)
        print(result, end='')