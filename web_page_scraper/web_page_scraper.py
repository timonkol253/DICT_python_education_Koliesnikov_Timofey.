import requests
from bs4 import BeautifulSoup
import string
import os

def save_article(article_url, article_title, page_number):
    """
    Завантажує та зберігає текст статті за вказаною URL-адресою.
    Стаття зберігається у вигляді текстового файлу в папці, що відповідає номеру сторінки.
    """
    try:
        response = requests.get(article_url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            article_body = soup.find('div', class_='body')

            if article_body:
                article_text = article_body.get_text().strip().replace('\n', ' ').replace('  ', ' ')
                clean_title = article_title.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_')
                file_name = f"Page_{page_number}/{clean_title}.txt"
                os.makedirs(os.path.dirname(file_name), exist_ok=True)

                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(article_text)

                print(f"Saved article: {file_name}")
            else:
                print(f"Article body not found for {article_title}.")
        else:
            print(f"Article page returned status {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article {article_title}: {e}")

def fetch_page_html(page_url):
    """
    Отримує та повертає вміст HTML веб-сторінки за допомогою BeautifulSoup.
    """
    try:
        response = requests.get(page_url, timeout=10)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            print(f"URL returned status {response.status_code} for {page_url}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_url}: {e}")
        return None

def filter_articles(articles, type_filter):
    """
    Фільтрує список статей за вказаним типом статті.
    """
    filtered = []
    for article in articles:
        article_type = article.find('span', {'data-test': 'article.type'})
        if article_type and article_type.get_text() == type_filter:
            filtered.append(article)
    return filtered

def process_page(soup, page_number, type_filter):
    """
    Обробляє одну сторінку, знаходить і зберігає відфільтровані статті.
    """
    articles = soup.find_all('article')
    filtered_articles = filter_articles(articles, type_filter)

    for article in filtered_articles:
        link = article.find('a', {'data-track-action': 'view article'})
        if link:
            article_url = 'https://www.nature.com' + link.get('href')
            article_title = link.get_text().strip()
            save_article(article_url, article_title, page_number)

def download_articles(url, total_pages, type_filter):
    """
    Завантажує та зберігає статті з кількох сторінок за допомогою фільтра заданого типу.
    """
    try:
        for page_number in range(1, total_pages + 1):
            page_url = f"{url}&page={page_number}"
            print(f"Fetching articles from {page_url}...")

            soup = fetch_page_html(page_url)

            if soup:
                os.makedirs(f"Page_{page_number}", exist_ok=True)
                process_page(soup, page_number, type_filter)

                print(f"Finished processing Page {page_number}.")
            else:
                print(f"Failed to process Page {page_number}.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles list: {e}")

def main():
    total_pages = int(input("Input the number of pages:\n> "))
    type_filter = input("Input the article type (e.g., 'Nature Briefing'):\n> ")

    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022"
    download_articles(url, total_pages, type_filter)

    print("Saved all articles.")

if __name__ == "__main__":
    main()
