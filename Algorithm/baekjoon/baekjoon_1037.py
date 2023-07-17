# 1037번 약수


sample = int(input())
n = 0
list_1 = []
list_1 = list(map(int,input().split()))
n_sell = list_1[0]
for i in range(sample):
    n1 = int(list_1[i])
    if n < n1:
        n = n1
    if n_sell > n1:
        n_sell = n1
big_number = (n * n_sell)
print(big_number)


#더 줄여보기

# a = int(input())

# b = list(map(int,input().split()))
# b.sort()
# print(b[0]*b[-1])

