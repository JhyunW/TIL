# SW Expert
# 쉬운 거스름돈

def change(n):
    all_list = []
    a = 0
    a = n // 50000
    print(a, end =' ')
    n = n - a * 50000

    a = n // 10000
    print(a, end = ' ')
    n = n - a * 10000

    a = n // 5000
    print(a, end = ' ')
    n = n - a * 5000

    a = n // 1000
    print(a, end = ' ')
    n = n - a * 1000

    a = n // 500
    print(a, end=' ')
    n = n - a * 500

    a = n // 100
    print(a, end=' ')
    n = n - a * 100

    a = n // 50
    print(a, end=' ')
    n = n - a * 50

    a = n // 10
    print(a, end=' ')


T = int(input())  # 테케

for tc in range(1, T+1):

    N = int(input())  # 돈 입력
    print(f'#{tc}')
    change(N)
    print()
