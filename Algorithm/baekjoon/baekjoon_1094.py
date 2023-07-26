
# X = 만들고싶은 막대의 길이
# 64 = 처음 막대의 길이
# X보다 작을시 절반을 자르고 반을 버리고를 반복

x = int(input())

first = 64

second = 32 # 반토막 후

alone = 0 # 결과저장

count = 1
if first == x:
     print(count)
else:
     alone = 32 # 반토막내고 시작
     while alone != x: # x랑 같아질때까지 반복
         if alone > x: # 길이가 목표보다 길때
             second = second / 2
             alone = alone - second
         elif alone < x: # 길이가 목표보다 짧을때
             second = second / 2
             alone += second
             count += 1
     print(count)


