# 오늘 하루 동안 팔린 책의 개수 N
N = int(input())
book_list = {}

for i in range(N) : 
    book = input()
    if book not in book_list : 
        book_list[book] = 1
    else : 
        book_list[book] += 1 

# 가장 많이 팔린 책 
# print(max(book_list))

# 가장 많이 팔린 책이 여러권일 경우 사전 순으로 가장 앞서는 제목
best_list = []
best = max(book_list.values())

for i in book_list :
    if best == book_list[i] : 
        best_list.append(i)
# print(best_list)
best_list.sort()
print(best_list[0])
