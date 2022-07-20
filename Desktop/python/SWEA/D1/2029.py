#2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성

import sys
sys.stdin = open("2029_input.txt", "r")

T = int(input()) # 3
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a,b = map(int, input().split())
    print("#%d" % test_case, end=" ")
    print(a // b, end=" ")
    print(a % b)