# SW Expert
#1244_최대 상금
import copy

def change(N, re):
    stack = [N]
    stack_ing = []
    for q in range(re):
        while stack:
            original = stack.pop(0)
            ori = copy.deepcopy(original)
            for w in range(len(original)-1):
                for w1 in range(w+1, len(original)):
                    ori[w], ori[w1] = ori[w1], ori[w]
                    stack_ing.append(ori)
                    ori = copy.deepcopy(original)
        stack = stack_ing
        stack_ing = []
    best = 0
    for e in stack:
        mid = ''
        for e1 in e:
            mid += e1
        if best < int(mid):
            best = int(mid)
    print(f'#{tc} {best}')



T = int(input())  # 테케
for tc in range(1, T+1):
    arr = [list(map(str, input().split()))]
    number = []
    for i in arr[0][0]:  # 리스트에 숫자를 하나씩 대입
        number.append(i)
    nu = copy.deepcopy(number)
    data = [0] * len(arr[0][0])

    change(number, int(arr[0][1]))