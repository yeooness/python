# 2
# I am happy today
# We want to win the first prize

# 띄어쓰기를 기준으로 잘라서 리스트에 담아주기 
t = int(input())
for test_case in range(t) : 
    word = list(input().split())
    for i in word : 
        print(i[::-1], end =' ')