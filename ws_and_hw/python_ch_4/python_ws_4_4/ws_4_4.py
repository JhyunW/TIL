import requests
from pprint import pprint as print

dummy_data = []
for i in range(10):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i+1}'

    response = requests.get(API_URL)
    parsed_data = response.json()

    dummy_data.append({'company' : parsed_data['company']['name'], 'lat' : parsed_data['address']['geo']['lat'], 'lng' : parsed_data['address']['geo']['lng'], 'name' : parsed_data['name']})

#print(dummy_data)
# --------------- 더미데이터 뽑기 -----------------------
black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']
company_test = []
def create_user(info):
    global company_test
    company_test.append({info['company'] : info['name']})
    return company_test

company_result = list(map(create_user,dummy_data))[0]  #고치는법 물어보기...

# print(company_result)



censored_user_list = {}

def censorship(company_result):
    for company_name in company_result:
        for key, value in company_name.items():
            if key not in black_list:
                print('이상 없습니다.')
                return True
            else:
                print(f'{key}소속의{value}은/는 등록할 수 없습니다.')
                censored_user_list[key] = [value]
                return False, censored_user_list
            
censorship(company_result)
print(censored_user_list)
