from bs4 import BeautifulSoup
import requests

class NewsScraper:
    def __init__(self, url):
        self.url = url

    def get_news(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        news = soup.find_all('div', class_='news-item')
        news_text = [item.text for item in news]
        return '\n'.join(news_text)
