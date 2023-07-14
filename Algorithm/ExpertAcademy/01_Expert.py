test = int(input()) #테스트 횟수


for z in range(test):

    n,m = map(int,input().split()) #배열 정의 #스프레이 세기
    
    list_01 = [[0] * 5 for z in range(n)]

    result_all = 0

    for i in range(n):
        list_01[i] = list(map(int,input().split()))

    for q in range(n):
        for w in range(n):
            result_p = 0
            result_x = 0

            result_p += list_01[q][w]
            result_x += list_01[q][w]
            for e in range(1,m):
                if q-e > 0 and w-e > 0:
                    #십자가 식
                    result_p += list_01[q-e][w]
                    result_p += list_01[q][w-e]
                    #x자 식
                    result_x += list_01[q-e][w-e]
                    result_x += list_01[q+e][w-e]
                if q+e < n and w+e < n:
                    #십자가 식
                    result_p += list_01[q+e][w]
                    result_p += list_01[q][w+e]
                    #x자 식
                    result_x += list_01[q+e][w+e]
                    result_x += list_01[q-e][w-e]
            
                #합산
                if result_p > result_x:
                    if result_p > result_all:
                        result_all = result_p
                elif result_p < result_x:
                    if result_x > result_all:
                        result_all = result_x
    
    print(result_all)
            