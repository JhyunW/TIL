#  백준
# 10973_이전 순열

def soonyul(arr, soon_list, soon_back):
  global use
  if len(arr) == N:
    soon_list = arr[:]
    if soon_list == now:
        if not soon_back:
          print(-1)
        else:
          print(soon_back)
        return
    else:
      soon_back = arr[:]
    return
  for i in range(N):
    if use[i] == 0:
      use[i] = 1
      arr.append(run[i])
      soonyul(arr)
      arr.pop()
      use[i] = 0

N = int(input())  # 자릿수
now = list(map(int, input().split()))  # 현재 순열, set으로 정렬
run = list(set(now))
use = [0] * N

soonyul([],0,0)
