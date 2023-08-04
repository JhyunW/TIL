tc = int(input())

for test in range(tc):
    number = int(input())

    numbers = list(map(int, input().split()))

    min_in = 0
    max_in = 0
    for i in range(1, number):
        if numbers[min_in] > numbers[i]:
            min_idx = i

        if numbers[max_in] <= numbers[i]:
            max_in = i
