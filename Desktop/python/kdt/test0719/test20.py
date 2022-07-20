# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

# number = int(input())
# sum = 0 

# for i in str(number) : 
#     sum += int(i) 
# print(sum)

# 풀이 1.
from math import remainder
from subprocess import REALTIME_PRIORITY_CLASS


number = int(input())
# number 가 0 일때 멈춤 -> Int는 0일때 False 가 되기 때문에
result = 0 
while number : 
    result += number%10 
    result //= 10

print(result)

#2.
# divmod(x,y)는 x를 y로 나누고 결과를 tuple로 반환
#(몫,나머지)
numer,remainder = divmod(number,10)
result += remainder
print(result)

