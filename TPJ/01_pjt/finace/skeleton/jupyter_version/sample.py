import pprint
import requests

def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "06842c54d0d16598423dd465287e7a43"
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    request = requests.get(url).json()
    print(request.keys())
    result = request['result']['baseList']

    return result

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)