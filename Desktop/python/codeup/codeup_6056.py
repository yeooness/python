# 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력

a, b = map(int, input().split())
print(bool(a) and bool(not b) or bool(not a) and bool(b))