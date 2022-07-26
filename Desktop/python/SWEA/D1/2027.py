for i in range(5) :
    for j in range(5) :
        if i == j :
            print('#', end='')
        else : 
            print('+', end ='')
    
    # i가 1일때 j의 for문이 다 돌면 바로 Print 해주기위해 
    print()