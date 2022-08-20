n, m = map(int,input().split())
dict_ = {}

#n의 크기만큼 듣도 못한 사람 입력
for i in range(n) : 
    p = input()
    dict_[p] = '듣도못한'
    # print(dict_)

list_ = []
#m의 크기만큼 보도 못한 사람 입력
for i in range(m) : 
    p = input()
    #입력받은 사람이 딕셔너리의 키 중에 있는지 화인 
    if p in dict_ : 
        list_.append(p)

list_.sort()
print(len(list_))
for p in list_ : 
    print(p)