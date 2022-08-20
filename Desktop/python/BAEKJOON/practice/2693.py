T = int(input())
for test_case in range(T) : 
    num = list(map(int,input().split()))
    
# 세번째로 큰 수 구하기 
    num.sort()
    print(num[-3])

