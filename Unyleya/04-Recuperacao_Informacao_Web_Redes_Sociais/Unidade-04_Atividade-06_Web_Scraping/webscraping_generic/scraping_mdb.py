# Import Libs
from bs4 import BeautifulSoup
import requests

# Definindo a URL
url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"

# Request do conteudo da URL
url_text = requests.get(url).text

# Parse do conteudo
url_texts = BeautifulSoup(url_text, 'html.parser')

for text in url_texts.find_all('a'):
    print(text.get('href'))
