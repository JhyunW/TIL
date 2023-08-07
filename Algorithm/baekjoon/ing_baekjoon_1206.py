# 백준 1421
# 나무꾼 이다솜

# 길이 - 기준cm  /  if 기준cm = 길이 노카운트에 갯수+1
# 기준>길이 노카운트 갯수도 노카운트

N, C, W = map(int, input().split())  # 나무갯수, 자르는비용, 나무cm당 가격

tree_tomak = 0
cut_count = 0
tree = []
for q in range(N):  # 나무 길이 입력
    tree.append(int(input()))
tree_min = min(tree)  # 가장 길이가 짧은 나무
tree_set = [] # 약수를 넣을 공간
for w in tree:  # 약수들의 리스트를 가장 길이가 작은나무를 기준으로  -1씩 해가며 구하기
    for e in range(tree_min, 0, -1):
        if w % e == 0:
            tree_set.append(e)

tree_center = max(set(tree_set))  # 가장 높은 최대 공약수

for r in tree:  # 최대 공약수로 자르면서 자른 횟수와 토막 갯수 구하기
    while r != 0:
        print('w')
        if r == tree_center:
            tree_tomak += 1
            r = r - tree_center
        else:
            tree_tomak += 1
            cut_count += 1
            r = r - tree_center

charge = cut_count * C
print(charge)
profit = tree_tomak * tree_center * W
print(profit)

result = profit - charge

print(result)