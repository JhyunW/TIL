############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def count_over_speed(speed_list):
    count_car = 0 # 위반한 차량을 카운트 하기 위한 함수
    
    for car in speed_list: # 리스트에 있는 각각의 수를 반복문 돌림
        if car > 100:  # 만약 속도가 100을 넘어가면
            count_car += 1 # 카운트가 1 증가
    return count_car # 총 카운트를 반환
    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(count_over_speed([119, 124, 178, 192,]))  #=> 4

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
