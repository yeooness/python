n = int(input())
number = list(map(int,input().split()))
new_num = sorted(number)
rank = n//2
print(new_num[rank])


