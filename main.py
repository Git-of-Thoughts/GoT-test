from news_scraper import NewsScraper
from email_sender import EmailSender

def main():
    news_scraper = NewsScraper('http://www.donews.com/news/')
    news = news_scraper.get_news()

    email_sender = EmailSender('sender_email', 'sender_password', 'cqtxh@163.com')
    email_sender.send_email('Daily Technology News', news)

if __name__ == '__main__':
    main()
