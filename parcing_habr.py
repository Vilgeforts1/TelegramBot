import requests
from bs4 import BeautifulSoup
import json


URL = 'https://habr.com/ru/news/'
HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


new_dict = {}
fresh_news ={}

def get_content():
    r = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    
    articles_news = soup.find_all('article', class_='tm-articles-list__item')
    for item in articles_news:
        articles_title = item.find('a', class_='tm-article-snippet__title-link').text.strip()
        article_url = 'https://habr.com' + item.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').get('href')
        article_date = item.find('time').get('title')

        article_id = article_url.split('/')
        article_id = list(filter(lambda x: x not in ('', ' '), article_id))[-1]

        new_dict[article_id] = {
            'articles_title': articles_title,
            'article_url': article_url,
            'article_date': article_date
        }

        with open('new_dict.json', 'w', encoding='utf-8') as file:
            json.dump(new_dict, file, indent=4, ensure_ascii=False)



def chek_new_news():
    with open('new_dict.json', encoding='utf-8') as file:
        new_dict = json.load(file)

    URL = 'https://habr.com/ru/news/'
    HEADERS = {
        'User-Agent':
            'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36',
        'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')

    articles_news = soup.find_all('article', class_='tm-articles-list__item')
    for item in articles_news:
        article_url = 'https://habr.com' + item.find('h2',class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').get('href')
        article_id = article_url.split('/')
        article_id = list(filter(lambda x: x not in ('', ' '), article_id))[-1]

        if article_id in new_dict:
            continue
        else:
            articles_title = item.find('a', class_='tm-article-snippet__title-link').text.strip()
            article_date = item.find('time').get('title')

            new_dict[article_id] = {
                'articles_title': articles_title,
                'article_url': article_url,
                'article_date': article_date
            }

            fresh_news[article_id] = {
                'articles_title': articles_title,
                'article_url': article_url,
                'article_date': article_date
            }

    with open('new_dict.json', 'w', encoding='utf-8') as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)

    return fresh_news



def main():
    get_content()
    chek_new_news()


if __name__ == '__main__':
    main()
