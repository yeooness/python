# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력
import sys
sys.stdin = open("1989_input.txt", "r")

T = int(input()) 
for test_case in range(1, T + 1):
    word = input()
    # reverse_word= ''
    # for i in word : 
    #     reverse_word = i + reverse_word
    # if word == reverse_word : 
    #     print('1')
    # else : 
    #     print('0') 
    
    if word == word[::-1] : 
        print(f'#{test_case} {1}')
    else : 
        print(f'#{test_case} {0}')



    