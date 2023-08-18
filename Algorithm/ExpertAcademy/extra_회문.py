T = int(input())

for tc in range(1, T+1):
    a = input()
    b = ''
    result = 0
    for i in a[::-1]:
        b += i
    if a == b:
        result = 1
        
    print(f'#{tc} {result}')