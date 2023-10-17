# N개의 정수로 이루어진 배열 A
# 이때 배열에 있는 정수의 순서를 적절히 바꿔 다음 식의 최댓값을 구하시오
# 기호가 절대값이였음..하...

from itertools import permutations
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
re = list(permutations(arr, N))  # 리스트 입력받은 숫자들을 N개를 사용해서 순열 생성

result = 0  # 최대숫자 저장 공간
for i in re:
  now = 0  # 현재 나오는 값
  for q in range(N-1):  # N-1 번째 까지 가는 반복문
    now += abs(i[q] - i[q+1])  # 해당 순열의 0~N-1 까지 모든 숫자의 절대값 넣기
  
  if result < now:  # 만약 나온 값이 현재의 최대값보다 높을 시 교체
    result = now
    # 다른 방법으로는
    # result = max(result, now)  로 매번 더 높은 값을 고를 수 있다.

print(result)