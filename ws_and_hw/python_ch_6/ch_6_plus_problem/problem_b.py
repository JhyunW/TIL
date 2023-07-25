# Q2. 다음은 학생들의 수학 점수를 나타낸 딕셔너리이다.
# 딕셔너리에 있는 점수 중, 80점 이상인 점수만을 가진 새로운 딕셔너리를 생성하는
# 함수 make_new_dict를 작성하시오.

scores = {
    'Alice': 75,
    'Bob': 92,
    'Charlie': 80,
    'David': 60,
    'Eva': 85
}

# 딕셔너리 안에 항목 추가 잊지말기 **
def make_new_dict(dict_in):
    score_80_up = {}
    for k,i in dict_in.items():
        if dict_in[k] >= 80:
            # score_80_up[i] = dict[i]
            score_80_up.setdefault(k,i)
    print(score_80_up)
    return score_80_up
# make_new_dict(scores) -> {'Bob': 92}

make_new_dict(scores)