# SW Expert
# 5248_그룹 나누기

# 풀이 방법은 교재에 존재


# 유니온 처리 -> 집합x와 지합y를 하나의 집합으로 연합 이루게 하기
def union(x, y):
    x = find_set(x)  # 실제 부모가 누구인지 찾으러 가기
    y = find_set(y)

    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y

    # 두 루트 노드의 rank가 동일 하다면,
    # 어디에 누구를 붙이든 똑같으니 하나 정해서 증가시켜준다.
    if rank[x] == rank[y]:
        rank[x] += 1
# 내 조상이 누군지 찾아가는 함수
# 루트 -> 자기 자신을 부모로 잡고 있는 노드가 될 때까지 조사
def find_set(x):
    if parent[x] == x:  # x노드의 부모가 자기자신 : 즉 x가 루트노드다
        return x
    
    else:
        return find_set(parent[x])

# 1 2 2 3
# [0 1 2 3]
# [0 1 1 3] | x = 1 y = 2
# [0 1 1 2] | x = 2 y = 3


# -> x, y 의 루트 노드가 누구인지 (집합의 대장이 누구인지 찾는 과정)
# 1 2 2 3
# [0 1 2 3]
# [0 1 1 3] | x = 1 y = 2
# [0 1 1 2] | x = 2(2번 노드 집합의 대장을 찾아반환) y = 3
# [0 1 1 1] | x = 1 y = 3 

T = int(input())  # 테케

for tc in range(1,T+1):
    N, M = map(int, input().split())  # N 과 M N번까지의 출석번호, M개의 제출종이
    arr = list(map(int, input().split()))  # 노드

    # 간선 정보를 모른다는 가정하에
    # 최초의 각 노드들의 정보를 초기화
    # make_set = 각각의 집합 생성하기

    parent = list(range(N+1))
    # 각 노드가 자식 노드를 얼마나 연결하고 있는지를 초기화
    rank = [0] * (N+1)


    for i in range(M):
        x = arr[i*2]
        y = arr[i*2+1]
        union(x, y)
    
    print(arr)
    print(set(parent))
    result = len(set(parent)) - 1
    print(f'#{tc} {result}')