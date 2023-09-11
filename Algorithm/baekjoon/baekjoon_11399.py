# 백준_11399번 ATM

# 매 시간 누적이 된다고 할 때
# 각 사람마다의 시간이 주어질 때 가장 최소의 시간이 걸리게끔
# 코드를 짜시오

human = int(input())

arr = list(map(int, input().split()))

a = sorted(arr)
print(a)
result = 0
all = 0
for i in range(human):
    result += a[i]
    all += result

print(all)