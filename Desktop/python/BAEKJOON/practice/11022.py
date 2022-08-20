T = int(input())
for test_case in range(1, T + 1): 
    a,b = map(int, input().split())
    # Case #x: A + B = C
    print(f'Case #{test_case}: {a} + {b} = {a+b}')