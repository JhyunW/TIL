# Q5. 2차원 리스트가 주어질 때, 2중 for문을 활용하면
# 행 → 우선 순회 | 열 ↓ 우선 순회를 자유롭게 진행 할 수 있다.
# 주어진 리스트이 행, 열 우선 순회 결과를 각각 출력하시오.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
list_num01 = []
list_num02 = []
for i in numbers:
    for z in i:
        list_num01.append(z)

print('-------------------------------------------')
for i2 in range(len(numbers)):
    for z2 in numbers:
        list_num02.append(z2[i2])

print(list_num01)
print(list_num02)

# 대각선 하는법!
for i in range(3):
    print(numbers[i][i], end = ' ')

for z in range(3):
    print(numbers[i],[3-(1+i)])
