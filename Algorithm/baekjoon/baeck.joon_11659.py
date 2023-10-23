# 백준 11659
# 구간 합 구하기4
# 시간복잡도를 줄이는 연습
# 합 배열을 이용해서 시간 복잡도를 줄여보기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 수의 개수, 계산 횟수
arr = list(map(int, input().split())) # 리스트 입력

for i in range(1, N):  # 배열의 합으로 변환해주기 각 배열에 더한 수를 놔두어 추가적인 계산을 안하도록 함
  arr[i] = arr[i-1] + arr[i]

for tc in range(M):  # 테스트케이스만큼 반복
  a, b = map(int, input().split())  # a~b까지의 합
  if a == 1:  # 배열1번일경우는 0으로 표시
    result = arr[b-1]
  else:
    result = arr[b-1] - arr[a-2]
  print(result)