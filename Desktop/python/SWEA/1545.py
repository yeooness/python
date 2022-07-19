# 주어진 숫자부터 0까지 순서대로 찍어보세요

n = int(input())
cnt = 0 

for i in range(n,-1,-1) :    #n번부터 / -1 :0번까지 / -1:거꾸로 출력
   print(i, end='')

