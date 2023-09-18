def quick_sort(arr):
    # 분할
    if len(arr) <= 1:
        return arr
    else:
        # 분할 작업
        pivot = arr[0]
        left,pivot_list, right = [], [], []
        for i in arr:
            if i > pivot:
                right.append(arr[i])
            elif i == pivot:
                right.append(arr[i])
            else:
                left.append(i)
        return quick_sort(left) + pivot_list + quick_sort(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
