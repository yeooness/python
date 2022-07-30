import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for test_case in range(1, T + 1) :
    # 입력 받을때 '-' 제거 
    num = input().replace('-', '')    
    
    # 길이가 16 이 아니거나 3,4,5,6,9로 시작하지않으면 카드 발급 불가 
    if len(num) != 16 or num[0] not in ['3','4','5','6','9'] :                  
        print(f'#{test_case}', 0)                                        
    else : 
        print(f'#{test_case}', 1) 
    
