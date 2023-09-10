<<<<<<< HEAD
# 2606_바이러스

# 한 컴퓨터가 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는
# 모든 컴퓨터는 웜 바이러스에 걸린다
# 1번 컴퓨터가 바이러스에 걸렸을 때 바이러스에 걸리게 되는 컴퓨터의 수를 구하는
# 프로그램을 작성



def bfs(n):
  marking[n] = 1  # 지나는 데이터 체크
  for i in data[n]:
    # n번째의 컴퓨터가 i번째와 연결되어 있고, 지나온 길에 기록이 없다면
    if not marking[i]:
      bfs(i)


com = int(input())  # 컴퓨터의 수

connect = int(input())  # 연결된 다리 수

arr = []  # 컴퓨터 연결정보를 쓸 곳

data = [[]for _ in range(com+1)]  # 연결 정보를 쓸 곳
marking = [0] * (com+1)  # 지나온곳을 표시할 변수
for _ in range(connect):
  arr.append(list(map(int, input().split())))  # 연결되어진 번호

for check in arr:
  data[check[0]] += [check[1]] 
  data[check[0]] += [check[1]]

bfs(1)
result = -1
for plus in range(1, com+1):
  result += marking[plus]

print(result)
=======
# 1124_언더프라임

# 예를들어 12를 소인수 분해하면 2, 2, 3 이 나오는데 이렇게 나온
# 숫자들의 갯수가 소수이면 그 수를 언더프라임 이라고 한다.
# A 보다 크거나 같고 B보다 작거나 같은 정수 범위 안에서 언더프라임인 것의 갯수를
# 구하시오

# 시간초과 해결해보기  count가 16개 이상이면 끝
A, B = map(int, input().split())  # 최소 A, 최대 B

prime = [0] * 100001
print(prime)
all_result = 0  # 최종결과

for i in range(2, 100000):  # 2부터 10000까지 확인
    print(i)
    count = 0 # 해당 숫자의 소수 갯수  즉 길이가 소수인지 확인 해야함
    now = i  # 현재 숫자
    div = 2  # 나눌 숫자 1은 안하므로 2 부터 시작해서 하나씩 늘려갈 예정
    while now != 1:  # 숫자가 나눠서 0이 될때까지
        if now % div == 0:  # 나눴을때 나머지가 없이 나눠지면
            now = now // div  # 그 값으로 나누기
            count += 1
        else:
            div += 1
        
        if div > 17 and count == 0:
            print(i)
            prime[i] = 1  # 17 이상까지 맞는게 없으면 프라임 이므로 체크
            break

        if now == 1:
            div = 2
            result = 0
            while count != 1:
                if count % div == 0:
                    result += 1
                    count = count // div
                else:
                    div += 1
                if result > 1:
                    break
                else:
                    prime[i] = 1

print(prime)

>>>>>>> a68886f7af3e470e9355bed6d80972d058c05865
