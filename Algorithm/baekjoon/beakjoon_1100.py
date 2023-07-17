ch_list = [[] * 8 for i in range(8)] #체스 판 생성

for z in range(8): # 체스 말 새우기
    line = " "
    line = str(input())
    ch_list[z] = line

#0,2,4,6 흰판
#1,3,5,7 흰판

count_01 = 0
for x in range(0, 8, 2):
    for c in range(8, 2):
        ch_one = ch_list[x][0][c : c+1]
        if ch_list[x][0][c : c+1] == "F":
            count_01 += 1

for v in range(1, 8, 2):
    for b in range(1, 8 ,2):
        ch_one = ch_list[v][0][b : b+1]
        if ch_one == "F":
            count_01 += 1

print(count_01)