# 백준 _ 2018
# 연속된 자연수의 합 구하기
import sys
input = sys.stdin.readline

N = int(input())  # N개의 순열

count = 1  # 카운팅
start_index = 1  # 시작 인덱스를 1로
end_index = 1  # 마지막 인덱스를 1로
sum = 1  # 합의 수를 1로 마지막 숫자 생각

while end_index != N:  # 끝 인덱스가 N이 아닐때까지
  if sum == N:  # 합이 같아지면
    count += 1  # 카운트를 1 올리고
    end_index += 1  # 끝 범위를 한칸 늘리고
    sum += end_index  # 총합에 더하기
  elif sum > N:  # 만약 현재의 합이 N보다 크면
    sum -= start_index  # 현재 시작 범위의 값을 합에서 빼주고
    start_index += 1  # 시작 범위를 한칸 올려준다
  else:
    end_index += 1  # 합이 N보다 작은 경우는 끝 범위를 1칸 올리고
    sum += end_index  # 끝 범위의 숫자를 더한다.

print(count)
