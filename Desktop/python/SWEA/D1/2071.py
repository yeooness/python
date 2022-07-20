# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)
import sys
sys.stdin = open("2071_input.txt", "r")

T = int(input()) 
for test_case in range(1, T + 1):
    number = list(map(int, input().split()))
    sum = 0 
    for i in number : 
        sum += i 
        total = round(sum/10)
    print("#%d" % test_case, end=" ")
    print(total)