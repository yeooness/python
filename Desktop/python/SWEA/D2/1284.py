import sys
sys.stdin = open("1284_input.txt", "r")

T = int(input()) 
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # P : a사 1l 요금  
    # Q : b사 기본요금 
    # R : 월간 사용량이 r 이하인 경우 기본요금 
    # S : r 이상이면 1l 당 + s 
    # W : 종민의 한달 수도양 w 리터 
    # P, Q, R, S, W(1 ≤ P, Q, R, S, W ≤ 10000, 자연수) 
    P, Q, R, S, W = map(int,input().split()) 
    A = P * W 
    if R > W : 
        B = Q
    else :
        B = Q + S * (W-R)
    print(f'#{test_case} {min(A,B)}')

    # A = P * W 
    # B = Q
    # if W > R : 
    #     B = (W-R) * S
    # if A > B : 
    #     print("#%d" % test_case, end=" ")
    #     print(B) 
    # else : 
    #     print("#%d" % test_case, end=" ")
    #     print(A)

