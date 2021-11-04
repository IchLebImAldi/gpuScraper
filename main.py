from bs4 import BeautifulSoup
import requests
from model.article import Article
from datetime import datetime
from secret import TOKEN, CHAT_ID

source = requests.get('https://t.me/s/HWL_GPU_Verfuegbarkeitshinweise').text
soup = BeautifulSoup(source, 'lxml')

with open('last_post.txt', 'r') as f:
    last_post = f.read()

articles = []

def send_msg(msg):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    params = {
        'chat_id': CHAT_ID,
        'text': msg
    }
    requests.get(url, params=params)

def is_new_post(post):
    # if time of old post is older than time of new post
    last_art = Article.from_string(last_post)

    last_art_date = datetime.strptime(last_art.date, '%d.%m.%Y - %H:%M:%S')
    post_date = datetime.strptime(post.date, '%d.%m.%Y - %H:%M:%S')

    return last_art_date < post_date and last_art.name != post.name
    
for article in soup.find_all('div', 'tgme_widget_message_wrap js-widget_message_wrap'):
    name = article.text.split('Name:')[1].split('Shop')[0].strip()
    shop = article.text.split('Shop:')[1].split('Preis')[0].strip()
    price = article.text.split('Preis:')[1].split('€')[0].strip()
    date = article.text.split('Datum:')[1].split('URL')[0].strip()
    url = article.text.split('URL:')[1].split('*')[0].strip()

    dic = {
        'name': name,
        'shop': shop,
        'price': price,
        'date': date,
        'url': url
    }

    art = Article.from_dict(dic)
    
    if is_new_post(art):
        print(art)
        if int(art.price.split(".")[0]) < 580:
            send_msg(art.prettify())
        
        articles.append(art)

with open('last_post.txt', 'w') as f:
    f.write(art.__str__())


