# 첫째 줄에 로그에 기록된 출입 기록의 수 n
n = int(input())
dic = {}
for i in range(n):
# n개의 줄에는 출입 기록이 순서대로
    p , c = input().split()
    if c == 'enter' : 
        dic[p] = 'enter'
    else : 
        del dic[p]
# print(dic)
# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 
dic = sorted(dic.keys(), reverse = True)
# 한 줄에 한 명씩 출력
for i in dic : 
    print(i)
