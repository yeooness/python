# i라는 숫자에 3 6 9 가 들어간 수 만큼 -출력, 띄어쓰기 없이
# 그 외에는 일반 숫자 출력

# 1. 
n = int(input())
for i in range(1, n+1): 
    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        print(i, end=' ')
    else:
        print("-" * clap, end=' ')

# 2.
N = int(input())
clap = ['3', '6', '9']

for i in range(1, N+1):
    count = 0
    for j in str(i):
        if j in clap:
            count += 1
    if count > 0:
        i = '-' * count
    print(i, end=' ')
