# problem1
```python
   def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "06842c54d0d16598423dd465287e7a43"
    
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    request = requests.get(url).json()  # 
    result = request['result'].keys()
    
    return result
```
  1. 부분에서 requests 로 받아오는걸 까먹어서 뭐가 잘못된건지 많이 고민했다 까먹지 말기
  2. 원하는 결과값 함수에 넣어서 쓰기
  3. key 값만 뽑는다는걸 이해를 잘못해서 keys() 함수를 빼먹음 주의하기


# problem2
```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "06842c54d0d16598423dd465287e7a43"
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    request = requests.get(url).json()
    result = request['result']['baseList']

    return result
```

1. 마찬가지로 리퀘스트 받는부분 잊지말걸
2. 딕셔너리 접속 방법 숙지할것

# problem3
```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "06842c54d0d16598423dd465287e7a43"
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    request = requests.get(url).json()
    key_result = request['result']["optionList"]
    result = []
    for i in key_result:
        code_dict = {'code': i['fin_prdt_cd']}
        result.append(code_dict) # fin_prdt_cd 만 뽑아서 리스트넣기


    return result
```
1. 새로운 시도로 원하는 값을 뽑아서 리스트 안에딕셔너리를 넣는 코드 숙지하기 처음 짜기가 어려웠음

# problem4
```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "06842c54d0d16598423dd465287e7a43"
    
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    request = requests.get(url).json() # json 형식으로 변환
    key_result = request['result'] # key 값이 result인 데이터를 변수에 저장
    key_result_baseList = key_result['baseList'] # baseList 데이터를 변수에 저장 - 순회
    key_result_optionList = key_result['optionList'] # optionList 데이터를 변수에 저장 - 금융상품코드 일치시

    result = [] # 최종 결과값 리스트 생성
    for base in key_result_baseList: # base 반복
        info =[] # option 에서 나온값 초기화 및 생성
        for option in key_result_optionList: # 옵션 리스트 포문 반복
            if base['fin_prdt_cd'] == option['fin_prdt_cd']: # 금융 코드가 같을시
                option_kr = {'저축 금리' : option['intr_rate'], # 맞는 값을 입력해서 딕셔너리로 저장
                             '저축 기간' : option['save_trm'],
                             '저축금리유형' : option['intr_rate_type_nm'],
                             '최고 우대금리' : option['intr_rate2']}
                info.append(option_kr) # 저장된 딕셔너리를 밖의 info 함수에 전달

        info_re = {'금리정보' : info,
                   '금융상품명' : base['fin_prdt_nm'],
                   '금융회사명' : base['kor_co_nm']} # 해당하는 base값의 값 딕셔너리로 저장
        result.append(info_re) # 두개의 딕셔너리를 합쳐 밖의 최종결과에 추가
                
                

    # result = 'result'
    
    return result
```
1. 최종 출력될 result 함수 생성
2. 처음 조건인 baseList 포문 생성 및 option에서 나온값을 저장 및 초기화 할 리스트 생성
3. 금융 코드가 같을시에 해당하는 데이터끼리 묶는 코드 생성
4. 나온 값들을 바로 밖의 포문 함수에 전달
5. 첫번째 포문 base 에서 원하는 데이터 값 딕셔너리로 출력 및 저장
6. 나온 결과값들 최종 결과 리스트에 합치기

## 어려웠던점들
  1. 딕셔너리끼리 합치기가 좀 힘들었음 딕셔너리 합치는 명령어 숙지하기
  2. 문제 이해도 부족 : 책을 많이 읽던가 해야함.