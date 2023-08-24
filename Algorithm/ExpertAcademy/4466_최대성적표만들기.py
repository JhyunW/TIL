# SW Expert
# 4466_최대성적표만들기

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())  # 과목수, 합칠수
    arr = list(map(int, input().split()))  # 점수 입력

    best = 0

    if len(arr) == 1:
        best = arr[0]
    else:
        for q in range(K):
            now_score = 0
            now_index = 0
            for q1 in range(len(arr)):
                if now_score < arr[q1]:
                    now_score = arr[q1]
                    now_index = q1
            arr.pop(now_index)
            best += now_score

    print(f'#{tc} {best}')