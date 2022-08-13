#  4 MISSPELL → MISPELL 의 경우 word=MISSPELL이라고 한다면, word[:3]=MIS, word[4:]=PELL 이므로, 
#  오타의 위치가 4인 경우 word[:3]+word[4:]를 출력하면 된다. 
#  즉 오타의 위치가 n이면 word[:n-1]+word[n:] 를 출력한다.

t = int(input())
for tc in range(t) : 
    n, word = input().split()
    n = int(n) 
    print(word[:n-1] + word[n:])