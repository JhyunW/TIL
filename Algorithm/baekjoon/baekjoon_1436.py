# 백준_1436
# 1로 만들기

# 정수 x에 사용할 수 있는 연산은 3가지
# x가 3으로 나누어 떨어지면 3으로 나눔
# 2로 나누어 떨어지면 2 로
# 1을 뺀다

a = int(input())  # 처음 입력받는 수

d = [0] * 1000001  # 메모지네이션

for i in range(2, a+1):
    li = [d[i-1]]
    if i % 3 == 0:
        li.append(d[i//3])
    if i % 2 == 0:
        li.append(d[i//2])
    d[i] = min(li) + 1
print(d[a])