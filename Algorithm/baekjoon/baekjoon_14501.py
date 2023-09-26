# 백준
# 14501_퇴사

def how(day, money):  
    global result
    for i in range(day, N):  # 해달 날부터 퇴사날까지
        if i + arr[i][0] <= N:  # 상담 소요가 N보다 작거나 같으면
            how(i+arr[i][0], money + arr[i][1])
    
    if money > result:
            result = money
            return  


N = int(input())  # 남은 일 수
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
    
how(0,0)

print(result)