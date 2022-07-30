import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    number = list(map(int,input().split()))
    # 소득의 평균 구하기
    sum_ = sum(number)
    avg_ = sum_ // N
    # print(avg_)
    
    # 소득 평균 이하인 사람 수 구하기 
    cnt = 0 
    for p in number :  
        if p <= avg_ : 
            cnt += 1 
    #print(cnt) 
    print(f'#{test_case} {cnt}')

    
