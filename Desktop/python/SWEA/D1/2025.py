# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
n = int(input())
cnt = 0 
for i in range(n+1) :
    cnt += i
print(cnt) 