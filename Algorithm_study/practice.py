# baekjoon
# 1932_정수 삼각형


n = int(input())  # 삼각형의 줄

arr = [[]for _ in range(n+1)]
for i in range(1, n+1):
    arr[i] = list(map(int, input().split()))

best_num = 0
print(arr)

visited = [0] * (n+1)
print(visited)

data = [[0]*(n+1) for _ in range(n+1)]
print(data)

