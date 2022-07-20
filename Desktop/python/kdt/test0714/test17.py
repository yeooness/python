# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
word = 'banana'
result = ''
for char in word:
    # 1. 알파벳을 숫자로 바꿈 
    number = ord(char)
    # 2. 숫자 -32 
    number = number -32 
    # 3. 다시 숫자를 알파벳으로
    result += chr(number)
print(result)