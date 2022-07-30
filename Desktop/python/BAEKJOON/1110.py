N = int(input())  #입력받은 값을 int로 바꿈
num = N           #변하는 값
count = 0         #몇 번 사이클인지
 
while True:
    a = num//10
    b = num %10
    c = (a+b)%10
    num = (b*10) + c
    count += 1
    
    if(num == N):
        break
 
print(count)

# 1. N과 num이 같아질때까지 while문을 돌린다.
# 2. 10의 자리 수를 구하는 것은 10으로 나눈 몫, 
#    1의 자리 수를 구하는 것은 10으로 나눈 나머지 를 활용하여 필요한 숫자를 만든다
# 3. 사이클이 돌때마다 count를 1씩 높인다.