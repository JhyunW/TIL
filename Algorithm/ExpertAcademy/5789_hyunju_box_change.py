# SW Expert
# 5789_현주의 상자 바꾸기

# 현주는 1번부터 N번까지 N개의 상자를 가지고 있고 각 상자는 처음 모두 0으로 적혀있다.
# 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려한다.
# L번 상자부터 R번 상자까지의 값을 i로 변경
# Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을
# 순서대로 출력

T = int(input())  # 테스트 케이스

for tc in range(1, T+1):
    N, Q = map(int, input().split())  # 상자의 갯수, 리롤 횟수
    arr = [0] * (N+1)  # N 개의 0이 들어간 상자 생성
    for i in range(1, Q+1):  # N번 숫자를 바꿔줌
        L, R = map(int, input().split())  # L부터R까지의 숫자를 i로 변경
        for q in range(L, R + 1):  # R번까지의 인덱스를 건드려야 하므로 R+1까지
            arr[q] = i  # arr[q]를 i값으로 변경
    
    print(f'#{tc}', end = ' ')  # 원하는 출력모습으로 나타내기 위해 end 를 공백으로 표시

    for w in range(1, len(arr)):  # arr의 1 번째부터 차례로 프린트 (0번은비어있음)
        print(arr[w], end = ' ')
    print()