# baekjoon
# 9095 _ 1,2,3 더하기

# 정수 n을 1,2,3 의 합으로 나타내는 방법을 구하시오

def plus(num):  # 직접 써보며 규칙을 찾아보니
    # (plus(num - 1) + plus(num - 2) + plus(num - 3) 의 공식이 나옴
    if num == 1:  # 1,2,3 의 경우는 기준 리턴값 저장
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4

    if num > 3:  # 3보다 커질시에 함수를 다시 불러내는 재귀함수 구현
        return (plus(num - 1) + plus(num - 2) + plus(num - 3))

T = int(input())  # 테스트 케이스
for tc in range(1, T+1):  # 테스트케이스 반복
    n = int(input())  # 값 입력

    print(f'#{tc} {plus(n)}')

