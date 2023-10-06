import matplotlib.pyplot as plt  # 메트폴립 임포트 받아오기

# 예제1: x, y, 가 같을 때
plt.plot([1,2,3,4])
# plt.show()

# 참고: 이때까지 그렸던 plot 지우기
plt.clf()

# 예제2:x,y 가 다를때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x, y)
# plt.show()
plt.clf()


# 예제3: 제목 + 각 축의 설명
plt.plot(x, y)
# 제목
plt.title("Test Graph")

# x, y 축
plt.ylabel('y label')
plt.xlabel('x label')

plt.show()
