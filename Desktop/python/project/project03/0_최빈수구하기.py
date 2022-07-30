import sys

sys.stdin = open("_최빈수구하기.txt")
T = int(input())
for test_case in range(1, T + 1):
    
    N = int(input()) #테스트케이스의 번호
    num = list(map(int, input().split()))
    #1부터 100까지 숫자의 개수를 체크할 0으로 이루어진 리스트 (점수는 0점 이상 100점 이하)
    score = [0]*101  
    # 1부터 100까지 리스트에 각각의 숫자가 몇개씩 있는지 담아준다 
    for i in num : 
        score[i] += 1 
    #print(score)

    # 리스트안 최대 숫자를 가진 인덱싱의 숫자가 최빈수
    max_ = max(score)
    result = []
    # 인덱싱의 숫자가 최대 숫자와 같으면 Result에 담아준 후 
    for i in range(len(score)) : 
        if score[i] == max_ :
            result.append(i)
    # print(result)
    # 최빈수가 여러개일땐 가장 큰 점수 출력 
    print(f'#{test_case} {max(result)}')