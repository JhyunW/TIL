import json
from pprint import pprint


def book_info(book, categories):
    book_teg_name = []
    for book_cate in categories:
        if book_cate['id'] in book['categoryId']:
            book_teg_name.append(book_cate['name'])
            
    book_info = {'id' : book['id'],
                 'name' : book["title"],
            'author' : book['author'],
            'priceSales' : book['priceSales'],
            'description' : book['description'],
            'cover' : book['cover'],
            'categoryName' : book_teg_name
            }
    
    return book_info
    # 여기에 코드를 작성합니다.  

        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
