# baekjoon_10799
# 쇠막대기
r = input()  # 레이저

n = 0  # 놓인 막대기 갯수
result = 0  # 토막 갯수

for i in range(len(r)):  # 하나씩 탐색
    if r[i] == '(':  # 만약 이번 순서가 ( 이고
        if r[i+1] == ')':
            continue  # 앞에 레이저가 있을시 논 카운트
        else:
            n += 1  # 앞에 레이저가 없을 시 카운트

    elif r[i] == ')':  # 닫는 괄호일 경우
        if r[i-1] == '(':  # 그 레이저일 경우 놓인 막대만큼 더하기
            result += n
        else:  # 토막이 끝날 경우 끝난 토막 끝자락 더하기
            result += 1
            n -= 1

print(result)