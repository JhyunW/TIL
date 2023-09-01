# SW Expert
# 1244_최대 상금
import copy


def change(N, re):
    stack = [N]
    stack_ing = set()
    for _ in range(re):
        for original in stack:
            original = list(original)
            ori = copy.deepcopy(original)
            for left in range(len(original) - 1):
                for right in range(left + 1, len(original)):
                    if ori[left] < ori[right]:
                        ori[left], ori[right] = ori[right], ori[left]
                        ori_str = ''.join(ori)
                        if ori_str not in stack_ing:
                            stack_ing.add(ori_str)
                        ori = copy.deepcopy(original)

        stack = list(stack_ing)

        if not stack:
            check = [0] * 10
            for n in ori:
                check[int(n)] += 1
                if check[int(n)] >= 2:
                    stack.append(ori)
                    break
            else:
                ori[-1], ori[-2] = ori[-2], ori[-1]
                stack.append(ori)
        stack_ing = set()

    best = 0
    for e in stack:
        best = max(best, int(''.join(e)))

    print(f'#{tc} {best}')


T = int(input())  # 테케
for tc in range(1, T + 1):
    number, r = input().split()

    # number = list(number)
    change(number, int(r))
