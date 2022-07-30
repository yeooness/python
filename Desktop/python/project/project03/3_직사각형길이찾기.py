import sys

sys.stdin = open("_직사각형길이찾기.txt")
T = int(input())
for test_case in range(1, T + 1) :
    n = list(map(int,input().split()))
    n.sort()
    # print(n)
    if n[0] != n[1] :
        print(f'#{test_case} {n[0]}')
        # print(n[0]) 
    if n[0] == n[1] : 
        print(f'#{test_case} {n[2]}') 
