# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

word = 'banana'

# 문자로 순회하는것이 아니라 인덱스로 접근해서!
# 원하는 숫자 0,1,2,3,4,5 
# 얻는 방법은 ? range(len(word))
for i in range(len(word)) : 
   # print(i, word[i])
   # 알파벳이 a 일때 
   if word[i] == 'a' : 
    print(i)
    break 
else : 
    print(-1)

# 추가 문제
# 문자열 word가 주어질 때, 해당 문자열에서 a 의 
# 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지
word = input()

for i in range(len(word)):
    if word[i] == 'a':
        print(i, end = '')


