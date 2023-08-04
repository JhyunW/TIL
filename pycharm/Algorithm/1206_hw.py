test_case = 10 # 테스트 케이스

for i in range(test_case):
    
    n = int(input()) # 건물의 갯수
    
    out_room = 0 # 뷰 좋은 집 갯수
    
    build = list(map(int, input().split())) # 건물 높이

    for index in range(2, n - 2):
        value = build[index]
        if value == 0:  # 앞의 두 개와 마지막 두 개를 빼고 포문을 돌림
         continue
        tall_build = max(build[index-2], build[index-1], build[index+1], build[index+2]) # 비교 건물중 가장 높은 건물
        build_range = value - tall_build  # 지금의 건물 안에서 범위-2~+2 사이의 오차
        
        if build_range > 0:
            out_room += build_range
            
    print(f'#{i+1} {out_room}')

