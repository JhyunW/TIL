# 백준 2621
# 카드게임

# 빨간색, 파란색, 노란색, 녹색의 네 가지 색이 있고, 색깔별로 1부터 9까지 숫자가 쓰여진 카드가 9장씩 있다.

import sys
input = sys.stdin.readline

arr = [list(map(str, input().split()))for _ in range(5)]
color = []
number = []
for i in range(5):
  color.append(arr[i][0])
  number.append(int(arr[i][1]))

list_co = list(set(color))
list_num = list(set(number))
best = 0

# 모두 같은색의 카드
if len(list_co) == 1:
  if len(list_num) == 5 and (list_num[-1] - list_num[0] == 4):  # 숫자가 순서대로 나열 1번케이스
    a = max(number) + 900
    best = max(best, a)
  else:  # 4번 케이스
    a = max(number) + 600
    best = max(best, a)

if len(list_num) == 5 and list_num[-1] - list_num[0] == 4:  # 5번 케이스
  a = list_num[-1] + 500
  best = max(best, a)

# 숫자가 같을경우
for q in range(1,10):
  cnt = number.count(q)

  if cnt == 4:  # 2번 케이스
    a = 800 + q
    best = max(best, a)
  
  if cnt == 3: 
    if len(list_num) == 2:  # 3장의 숫자가 같고 나머지 2장도 같을경우 3번 케이스
      list_num.remove(q)
      a = q * 10 + list_num[0] + 700
      best = max(best, a)
    else:  # 6번 케이스
      a = q + 400
      best = max(best, a)
  
  if cnt == 2:
    if len(list_num) == 3:  # 2장이 같고 또 다른 2장이 같을경우 7번 케이스
      for w in range(q+1, 10):
        cnt2 = number.count(w)
        if cnt2 == 2:  # 7번 케이스 2장 2장
          val_up = max(q, w)
          val_min = min(q, w)
          a = val_up * 10 + val_min + 300
          best = max(best, a)
    if len(list_num) == 4:  # 2장만 같은경우 8번케이스
      a = q + 200
      best = max(best, a)
a = list_num[-1] + 100
best = max(best, a)

print(best)