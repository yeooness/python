# 01 Hello World!를 출력하시오.
print('Hello World!')

# 02 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력
print('강한친구 대한육군\n강한친구 대한육군')

# 03 고양이 출력 
print('\\    /\\')
print(" )  ( ')")
print('(  /  )')
print('\\(__)|')

# 04 강아지 출력 
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

# 05 두 정수 A와 B를 입력받은 다음, A+B를 출력
a,b = map(int,(input().split()))
print(a+b)

# 06 두 정수 A와 B를 입력받은 다음, A-B를 출력
a,b = map(int,(input().split()))
print(a-b)

# 07 두 정수 A와 B를 입력받은 다음, A*B를 출력
a,b = map(int,(input().split()))
print(a*b)

# 08 두 정수 A와 B를 입력받은 다음, A/B를 출력
a,b = map(int,(input().split()))
print(a/b)

# 09 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력
a,b = map(int,(input().split()))
# #sep 은 출력문들 사이에 해당내용 추가
print(a+b, a-b, a*b, a//b, a%b, sep='\n') 
 
# 10 ??!
print(input()+'??!')

# 11 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램
# 불기연도와 서기연도는 543년 차이 
print(int(input()) -543)

# 12 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력
A,B,C = map(int(),input().split())
print((A+B)%C, ((A%C) + (B%C))%C,(A*B)%C, ((A%C) * (B%C))%C, sep='\n')

# 13









