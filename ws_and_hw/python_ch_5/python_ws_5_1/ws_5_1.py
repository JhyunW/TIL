# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(rev):
    # 뒤집힌 문자열 리스트로 교체 메서드 활용x
    reverse_list = list(reversed(rev))

    # 최종 결과값
    result =' '

    for char  in reverse_list:
        result = result + char
        #print(result)

    #'{seperator}'.join(iterable)
    # '-'.join([1, 2, 3, 4, 5])
    # >>> '1-2-3-4-5'
    # result = "".join(reversed(rev)) 메서드를 활용한 첫번째 방법
    
    return result

result = reverse_string("Hello, World!")
print(result)