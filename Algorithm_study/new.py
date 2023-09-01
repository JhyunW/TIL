W = list(map(int, input().split()))  # 컨테이너의 무게
T = list(map(int, input().split()))  # 트럭의 적재용량

a = sorted(W)
b = sorted(T)
print(a)
print(b)