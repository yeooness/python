n = []
for i in range(10) : 
    n.append(int(input()))
# print(n)
# 평균 
print(sum(n) // 10)

# 최빈값
print(max(n, key = n.count))
