word_len = 4
e_arr = []
arr = [['abcdef'],['ghijkl'],['abcdef'],['qwerty'],['abcdef'],['abcdef']]
for e in range(6 - word_len + 1):  # 세로열 비교
    e_arr = []
    for e_1 in range(6):
        e_str = ''
        for e_2 in range(word_len):
            e_str += arr[e + e_2][e_1]

        print(e_arr)