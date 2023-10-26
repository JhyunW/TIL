# 백준_16918
# 봄버맨

# R * C인 직사각형 격자판
# 3초 카운트 후폭탄이 터지면 있던 칸과 인전한 네 칸도 함께 파괴
# 만약 인접한 칸에 폭탄이 있는경우 폭탄은 폭발 없이 파괴
# 봄버맨은 모든칸을 자유롭게 이동
# 가장 처음 봄버맨은 모든 칸에 폰탄을 설치
# 다음 1초동안 아무것도 안함
# 다음 2초동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치
# 1초가 지난 후에 3초전에 설치된 폭탄이 모두 폭발
# 다시 1초동안 아무것도 안함.
# 다음1초동안 모든 칸에 폭탄 설치

dx = [1, 0, -1, 0]  # 상하좌우
dy = [0, 1, 0, -1]

R, C, N = map(int, input().split())  # R * C 판 , N 초

arr = [list(input()) for _ in range(R)]  # 봄버판 받아오기
data = [[0]*C for _ in range(R)]  # 시간을 잴 판
for heigh in range(R):
  for length in range(C):
    if arr[heigh][length] == 'O':  # 폭탄 있는 장소
      data[heigh][length] = 2  # 폭탄 시간 넣기

pattern = 0  # 멍, 설치, 폭발
for i in range(N):  # i초 지남
  pattern += 1
  for j in range(R):  # j줄
    for q in range(C):  # r열
      if data[j][q] != 0 : # 폭탄이 있다면
        data[j][q] = data[j][q] - 1

      if pattern == 1:  # 설치
        if arr[j][q] == '.':  # 비어있다면
          arr[j][q] = 'O'  # 설치
          data[j][q] = 2  # 시간초도 설정

      elif pattern == 2 and data[j][q] == 0:  # 폭발 xxxx
        data[j][q] = 0
        arr[j][q] = '.'
        for a in range(4):
          nx, ny = j+dx[a], q+dx[a]
          if 0 <= nx < R and 0 <= ny < C: 
            data[nx][ny] = 0    
            arr[nx][ny] = '.'
  if pattern == 2:
    pattern = 0
print(arr)

      
        



