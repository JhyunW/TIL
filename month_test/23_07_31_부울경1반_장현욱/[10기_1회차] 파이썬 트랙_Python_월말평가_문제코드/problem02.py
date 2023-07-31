############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_average(speed_list):
    car_speed_plus = 0 # 위반한 차의 속도를 모두 더할 함수
    car_count = 0 # 위반한 차의 대수를 세는 함수
    for car_speed in speed_list: # 반복문
        if car_speed > 100: # 자동차의 속도가 100을 넘어가면
            car_speed_plus += car_speed # 자동차의 속도를 car_speed_plus 함수에 더함
            car_count += 1 # 자동차 카운트 1 증가
    
    car_result = car_speed_plus / car_count # 총 더한 값 / 위반한 자동차의 대 수
    
    return car_result # 나온 결과를 반환
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calc_average([119, 124, 178, 192,]))  #=> 153.25
    
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    