n,m = map(int,input().split()) # 끊어진 줄의 갯수, 비교할 브랜드 갯수

brand  = [[] for z in range(m)] # 리스트 칸 생성

for i in range(m):
    brand_menu = list(map(int,input().split()))
    brand[i] = brand_menu #브랜드별 6줄의 가격, 1줄의 가격입

small_only = brand[0][-1] # 낱개중 저가
small_set = brand[0][0] # 패키지(6)중 저가

for x in range(m): # 작은 수 골라내기
    if small_only > brand[x][-1]:
        small_only = brand[x][-1]
    if small_set > brand[x][0]:
        small_set = brand[x][0]

all_list = [] # 상황별 최소 가격을 넣을 리스트
set_how = 0 # 세트 갯수
set_how_count = 0 # 몇 세트를 사야할지 갯수
while n >= set_how: # 사야할 셋트 구하는 조건문, 1개 이상
    set_how += 6
    set_how_count += 1

small_only_result = 0 # 낱개로만 샀을때 넣을 공간
small_set_only = 0 # 세트로만 샀을때 넣을 공간

small_only_result = small_only * n # 낱개로만 샀을때의 최저가
small_set_only = small_set * (set_how_count) # 패키지로만 샀을떄의 최저가
small_set_two = small_set * (set_how_count - 1) + (n - ((set_how_count - 1) * 6)) * small_only # 패키지 + 낱개 최저가
if set_how_count > 1: # 세트 구입 갯수가 2개가 안되면 낱개만 구매했을때랑 세트만 구매 했을 떄를 비교하면 됨
    all_list.append(small_only_result)
    all_list.append(small_set_only)
    all_list.append(small_set_two)

    print(min(all_list))

else: #낱개가 2개가 안될떄
    all_list.append(small_only_result)
    all_list.append(small_set_only)

    print(min(all_list))
