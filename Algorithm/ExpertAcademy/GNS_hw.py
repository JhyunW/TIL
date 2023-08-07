# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN" 를 크기 순으로 정렬
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    tc_num, number = map(str, input().split())

    # 딕셔너리를 만들어서 넣자
    number_dict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0
}
    
    arr = list(map(str, input().split()))

    for q in arr:
        number_dict[q] += 1

    print(tc_num, end = ' ')
    for w in number_dict:
            for e in range(number_dict[w]):
                print(w, end= ' ')
    
    # result = []

    # for key, value in number_dict:
    #     if value != 0:
    #         for w in range(value):
    #             result.append(key)

    # print(tc_num, *result)