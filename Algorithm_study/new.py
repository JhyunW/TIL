# SW Expert
# 토너먼트 카드게임

# 1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다
# 두개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자
# N 명의 학생들이 카드를 골랐을때 1등을 찾는 프로그램을 만드시오

T = int(input())  # 테케

for tc in range(1, T+1):
    N = int(input())  # 인원수 입력

    arr = list(map(int, input().split()))  # 카드 번호

    for i in range(len(arr)):  # 내는것과 선수번호
      arr[i] = [arr[i], i+1]

      winner = []  # 승자를 차례로 추가할 리스트
    
    while len(arr) != 1:
      a = arr.pop(0)  # 뭐를 냈는지, 몇번선수인지
      b = arr.pop(0)

      if a[0] == 1:  # 가위 일시
        if b[0] == 2:  # 후순위가 이길시
          winner.append(b)
        else:  # 나머지 경우
          winner.append(a)
      
      elif a[0] == 2: # 바위 일시
        if b[0] == 3:  # 후순위가 이길시
          winner.append(b)
        else:  # 나머지 경우
          winner.append(a)
      
      elif a[0] == 3:  # 보 일시
        if b[0] == 1:  # 후순위가 이길시
          winner.append(b)
        else:  # 나머지의 경우
          winner.append(a)

      if len(arr) == 1:
        a = arr.pop(0)
        if (b[0] - a[0]) % 3 == 2 :
          winner.append(a)
        else:
          winner.append(b)
      
      if not arr:
        if winner:
          arr.extend(winner)

    
    print(f'#{tc} {arr[0][1]}')

