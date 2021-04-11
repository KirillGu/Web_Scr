import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru/all/'
NT = '\n'
interesting_articles = []

keywords_lower = [element.lower() for element in KEYWORDS];
print('Ищем по ключевым словам: ', keywords_lower)

# URL
result = requests.get(URL)
soup = BeautifulSoup(result.text, 'html.parser')


# Articles
articles2 = soup.find_all('article', class_='post post_preview')
intext_words = []
for article in articles2:
    #print(article)
    for word in KEYWORDS:
        if word.lower() in article.text.lower():
            is_relative = True
            intext_words.append(word)

            url_element = article.find('a', class_='post__title_link')
            url = url_element.attrs.get('href')
            name = url_element.text

            date_element = article.find('span', class_='post__time')
            date = date_element.text
            print(f'{NT}Найдена статья, которая соответствует заданным ключевым словам: {NT}{date} - {name} - {url}')
            interesting_articles.append([date, name, url])

print(f'{NT}Cтатьи, которые соответствуют заданным словам в тексте: {len(interesting_articles)} шт. {NT}{interesting_articles}')
