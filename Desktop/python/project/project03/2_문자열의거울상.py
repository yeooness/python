import sys

sys.stdin = open("_문자열의거울상.txt")
T = int(input())
for test_case in range(1, T + 1):
    word = input() 
    result = ''
    for i in range(len(word)) : 
        if word[i] == 'b' :
            result += 'd'
        elif word[i] == 'd' : 
            result += 'b' 
        elif word[i] == 'p' :
            result += 'q' 
        elif word[i] == 'q' :
            result += 'p'
    # print(result)
    # print(result[::-1])
    print(f'#{test_case} {result[::-1]}')