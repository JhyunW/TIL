def soonyul(arr, soon_back, use):
    if len(arr) == N:
        if arr == now:
            if arr == run:
                return -1
            else:
              return soon_back
        else:
            return arr[:]

    for i in range(N):
        if not use[i]:
            use[i] = 1
            arr.append(run[i])
            soon_back = soonyul(arr, soon_back, use)
            arr.pop()
            use[i] = 0

    return soon_back

N = int(input())  # 자릿수
now = list(map(int, input().split()))  # 현재 순열, set으로 정렬
run = sorted(set(now), reverse=True)
soon_back = []
use = [0] * N

result = soonyul([], soon_back, use)

if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))
