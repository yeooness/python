# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

# number = 123
# import math
# digits = int(math.log10(n))+1

# print(digits)

number = int(123)
count=0

while(n>0):
    count=count+1
    n = n//10
print(count)

#풀이
number = 123
cnt = 0 
# 몫이 0이 되면 종료해야함 
# 0이되면 false 
while number : 
#while number != 0 : 
    number //= 10 
    cnt += 1
print(cnt)

