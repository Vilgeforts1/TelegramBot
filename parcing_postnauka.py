import requests
from bs4 import BeautifulSoup
import requests
import json


url = 'https://postnauka.ru/courses/'
headers = {
    'user-agent':
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36',
    'accept': '*/*'
}


dict_courses = {}


# ПОЛУЧЕНИЕ ИНФОРМАЦИИ И СОХРАНЕНИЕ В СЛОВАРЬ 
def get_content():
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    names_courses = soup.find_all('div', class_='cards-grid__card')
    for item in names_courses:
        dict_keys = {}
        dict_keys['NAME_COURSE'] = item.find('a', class_='course-card__title').text
        dict_keys['URL'] = 'https://postnauka.ru' + item.find('a', class_='course-card__title').get('href')
        dict_keys['PICTURE'] = item.find('img', class_='cg-background__fallback-img').get('src')
        dict_keys['NUMBER_VIDEO'] = item.find('div', class_='course-card__info').text
        dict_courses[item.find('a', class_='course-card__title').text] = dict_keys
        
    return dict_courses


# СОХРАНЕНИЕ СЛОВАРЯ В JSON
def save_json():
    with open('postnauka_dict.json', 'w', encoding='utf-8') as file:
        json.dump(get_content(), file, indent=4, ensure_ascii=False)
    





if __name__ == '__main__':
    save_json()
    get_content()
    