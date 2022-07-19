# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램 작성
import sys
sys.stdin = open("2070_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a,b = map(int, input().split())
    if a > b :
        print("#%d" % test_case, end=" ")
        print('>')
    elif a < b : 
        print("#%d" % test_case, end=" ")
        print('<')
    elif a == b : 
        print("#%d" % test_case, end=" ")
        print('=')
