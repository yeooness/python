# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

number = int(input())
sum = 0 

for i in str(number) : 
    sum += int(i) 
print(sum)

