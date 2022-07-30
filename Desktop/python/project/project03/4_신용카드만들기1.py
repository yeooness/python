import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for test_case in range(1, T + 1) :
    card = list(map(int,input().split()))
    # print(card)
    sum_ = 0 
    for i in range(len(card)):
        # 홀수일때 
        if(i+1) % 2 == 1 :
            sum_ += card[i] * 2 
        # 짝수일때
        else : 
            sum_ += card[i]
    #print(sum_)
        
    if sum_ % 10 == 0 :
        result = 0
    else : 
        result = 10 - (sum_ % 10) 
    print(f'#{test_case} {result}')
    
