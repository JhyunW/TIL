############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):
    result = ' ' # 결과를 넣을 공간
    for i in word: # 문자를 한 글자씩 반복
        change_chr = ord(i) # 숫자로 반환
        
        for z in range(num): # 입력한 num 숫자만큼 반복
            change_chr += 1 # 카운트 떄마다 chr의 넘버를 1씩 올려줌
        
            if change_chr >= 97 and change_chr <= 123: # 소문자일시
                if change_chr > 122: # 122를 넘어가면 97로 반환
                    change_chr = 97
            
            elif change_chr >= 65 and change_chr <= 91: # 대문자일시
                if change_chr > 90: # 90 을 넘어가면 65로 반환
                    change_chr = 65
            
        result += chr(change_chr) # chr로 반환해서 결과에 추가
    
    return result
    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    