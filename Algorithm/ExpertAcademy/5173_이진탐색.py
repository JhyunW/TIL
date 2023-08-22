# 팁!!!! 왼쪽 자식은 부모의*2 이고 오른쪽은 부모의*2+1

def inorder(node):
    global count
    if node <= N:
        # 안쪽 자식
        inorder(node * 2)
        inorder(node * 2 + 1)
        # tree에 값 할당
        tree[node] = count # 조건에 할당했을때 1 입력
        count += 1  # 그 후 카운트 증가
        inorder(node * 2 + 1)  # 오른쪽 확인


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # root를 1로 한다
    # 트리는 N+1개만큼 담을 수 있어야 함
    tree = [0] * (N-1)
    # 입력할 값
    count = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')