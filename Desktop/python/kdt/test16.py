m = {"a":0, "e":0, "i":0, "o":0, "u":0}
word = list(input())
cnt = 0 

for i in word :
    for n in m : 
        if i == n :
            cnt += 1
print(cnt)

# 풀이
#1.
word = 'apple'

cnt = 0
for char in word : 
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
        cnt += 1 
print(cnt)        

#2.
word = 'apple'

cnt = 0
for char in word :
    if char in 'aeiou' :
        cnt += 1
print(cnt)