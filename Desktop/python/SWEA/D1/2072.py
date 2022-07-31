# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력
t = int(input())
for test_case in range(1, t+1) : 
    number =  map(int, input().split())
    sum_ = 0

    for i in number : 
        if i % 2 == 1 : 
            sum_ += i 
    print(f'#{test_case} {sum_}')