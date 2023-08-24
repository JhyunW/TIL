# SW Expert
# 5431_민석이의 과제 체크하기

T = int(input())

for tc in range(1, T+1):  # 테케 반복
    N, K = map(int, input().split())  # 총 학생수와 제출 학생 수
    arr = list(map(int, input().split()))  # 제출학생 번호
    no = []  # 안낸 사람 리스트

    for i in range(1, N+1):  # 제출 목록에 없는 사람 골라내기
        if i not in arr:
            no.append(i)

    print(f'#{tc}', end = ' ')
    for q in no:
        print(f'{q}', end = ' ')
    print()