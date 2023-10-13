from bs4 import BeautifulSoup
from selenium import webdriver

def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    # 크롬 브루우조가 열림
    # 이때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    # print(html)
    soup = BeautifulSoup(html, "html.parser")

    # 검색 결과 가져오기
    # duv 태그 안의 id가 result-stats 라는 요소
    result_stats = soup.select_one("div#result-stats")
    print(result_stats.text)



get_google_data('파이썬')