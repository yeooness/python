n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) : 
    a[i] = int(a[i])

min = a[0]
for i in range(n):
    if min > a[i] : 
        min = a[i] 
print(min)