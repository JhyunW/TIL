# SW Expert
# 4869_ 종이붙이기
# 10 * 20, 20 * 20 종이들이 있음, 이 종이들을 이용하여
# 20 * N 크기의 직사각형을 채우는 방법의 갯수


def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return (paper(n-2) * 2) + paper(n-1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = int(N // 10)
    print(f'#{tc} {paper(a)}')