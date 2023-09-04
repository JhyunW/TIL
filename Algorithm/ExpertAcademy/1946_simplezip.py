# SW Expert
# 1946 간단한 압출 풀기
T = int(input())  # 테케

for tc in range(1, T+1):
    N = int(input())  # 압축풀이를 할 갯수

    arr = [list(map(str, input().split())) for _ in range(N)]  # 압축 풀 리스트입력

    print(f'#{tc}')

    line_count = 0
    for zip in arr:  # 압축파일들
        for number in range(int(zip[1])):
            print(zip[0], end='')
            line_count += 1
            if line_count == 10:
                print()
                line_count = 0
    print()