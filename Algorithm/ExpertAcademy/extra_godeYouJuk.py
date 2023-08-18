T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    arr = [[] for _ in range(N)]
    
    for i in range(N):
        arr[i].extend(list(map(int, input().split())))
    
    
    best = 0
    
    
    for q in range(N):
        count = 0
        for w in range(M):
            if arr[q][w] == 1:
                count += 1
                if best < count:
                    best = count
            elif arr[q][w] == 0:
                count = 0
    
    for q1 in range(M):
        count = 0
        for w1 in range(N):
            if arr[w1][q1] == 1:
                count += 1
                if best < count:
                    best = count
            elif arr[w1][q1] == 0:
                count = 0
                
    print(f'#{tc} {best}')