# SW Expert
# 5097_회전

# N개의 수열이 있다.
# 맨앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을때
# 맨 앞의 숫자는?

T = int(input())  # 테케입력

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N, M입력

    arr = list(map(int, input().split()))  # 배열 입력

    for i in range(M):
        a = arr.pop(0)  # 맨 앞 숫자
        arr.append(a)  # 그 숫자를 뒤에 더해줌

    print(f'#{tc} {arr[0]}')