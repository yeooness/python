# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

word = input()

for i in word : 
     # 대문자 a 는 65 
    print(ord(i) - 64, end = ' ')