import requests
from bs4 import BeautifulSoup

def ceawling_basic():
    # 가져올 웹 피이지 url
    url = 'https://quotes.toscrape.com/'

    response = requests.get(url)

    # 우리가 얻고자 하는 HTML 내용이 여기에 담긴다.
    html_text = response.text

    # HTML을 파싱이 가능한 정리된 형태로 변환
    soup = BeautifulSoup(html_text, 'html.parser')

    # 예브게 출력
    # print(soup.prettify())

    # 1. 태그로 검색하기
    # 1.1 가장 첫 번째 태그
    # 크롤링 할 때는 항상 페이지 분석 -> 검색
    title = soup.find('a')  # find함수로 검색해서 첫번째로a태그가 나오는것을 가져와라
    print(f'제목 : {title.text}')

    # 1.2 해당 태그 모든 요소
    a_tags = soup.find_all('a')  # a태그가 들어간 모든 것을 찾아라
    for a_tag in a_tags:
        print(f'링크 : {a_tag}')


    # 2. CSS 선택자로 검색하기
    # 2.1 첫 번째로 CSS 선택자와 일치하는 요소
    word = soup.select_one('.text')
    print(f'첫 번째 글 = {word.text}')

    # 2.2 CSS 선택자와 일치하는 모든 요소
    words = soup.select('.text')
    for w in words:
        print(f'글 : {w.text}')

    # 2.2 

    # 3. 


ceawling_basic()
