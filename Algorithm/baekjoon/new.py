arr = [list(map(str, input().split()))for _ in range(5)]
color = []
number = []
for i in range(5):
  color.append(arr[i][0])
  number.append(int(arr[i][1]))

print(color)
print(number)