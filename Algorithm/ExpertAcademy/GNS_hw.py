# 1221
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN" 가 크기 순서임
# 테스트 케이스의 번호, 공백문자 후 테스트 케이스가 주어짐
# ex) SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV ONE SVN ONE ONE FIV TWO SVN SIX ONE FOR TWO THR TWO TWO ONE SIX EGT
import sys
sys.stdin = open("input.txt")  # 입력해야 하는게 많아서 메모장으로 받아옴

T = int(input())  # 테스트 케이스 입력

for tc in range(T):  # 테스트 케이스 반복문
    tc_num, number = map(str, input().split())  # 테스트 케이스의 번호와 주어질 문장의 갯수 입력

    # 나올 문장이 정해져 있어 딕셔너리를 만들어서 넣었음, 처음엔 리스트로 뽑아냈는데 런타임 이였나 떠서 바꿈...
    number_dict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0
}
    
    arr = list(map(str, input().split()))  # 리스트에 문장들 입력

    for q in arr:  # 문장들을 반복
        number_dict[q] += 1  # 딕셔너리에 해당 key문자가 나올때마다 1을 더해줌

    print(tc_num, end = ' ') 
    for w in number_dict:
            for e in range(number_dict[w]):# 오류를 해결한 구간 / 리스트에 넣어서 한번에 출력할려고 하니까 메모리가 딸림..
                print(w, end= ' ')  # 매번 값을 받을때마다 따로 리스트에 넣지 않고 그때그때 출력을 해줌
    
    # result = []

    # for key, value in number_dict:
    #     if value != 0:
    #         for w in range(value):
    #             result.append(key)

    # print(tc_num, *result)