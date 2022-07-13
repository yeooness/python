# 소수점 이하의 수를 모두 버리고 몫만 나타낼 때 // 

month = int(input())

if month // 3 == 1 : 
    print('spring')
elif month // 3 == 2 : 
    print('summer')
elif month // 3 == 3 : 
    print('fall') 
else : 
    print('winter')
