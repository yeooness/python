# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

# number = int(input())

# while number > 0:
#     print(number%10, end='')
#     number //= 10

# 풀이
number = 123
result = 0 

while number : 
    # 이전 결과에 10을 곱하고
    result *= 10
    # 나머지를 더하고
    result += number%10
    #number를 깎는다
    number //= 10

print(result)