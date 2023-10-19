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

    # 보기 좋게 출력
    print(soup.prettify())



get_google_data('파이썬')