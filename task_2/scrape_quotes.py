import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "http://quotes.toscrape.com"

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def scrape_quotes():
    quotes = []
    authors = {}
    
    page = 1
    while True:
        soup = get_soup(f"{BASE_URL}/page/{page}/")
        quote_elements = soup.select(".quote")
        
        if not quote_elements:
            break
        
        for quote_element in quote_elements:
            quote_text = quote_element.find(class_="text").get_text(strip=True)
            author_name = quote_element.find(class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote_element.find_all(class_="tag")]
            
            # Додаємо цитату до списку цитат
            quotes.append({
                "tags": tags,
                "author": author_name,
                "quote": quote_text
            })
            
            # Якщо автора ще немає в словнику авторів, скрапимо дані про автора
            if author_name not in authors:
                author_url = BASE_URL + quote_element.find("a")["href"]
                authors[author_name] = scrape_author_details(author_url)
        
        page += 1
    
    return quotes, list(authors.values())

def scrape_author_details(url):
    soup = get_soup(url)
    fullname = soup.find(class_="author-title").get_text(strip=True)
    born_date = soup.find(class_="author-born-date").get_text(strip=True)
    born_location = soup.find(class_="author-born-location").get_text(strip=True)
    description = soup.find(class_="author-description").get_text(strip=True)
    
    return {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }

def save_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    quotes, authors = scrape_quotes()
    save_to_json('quotes.json', quotes)
    save_to_json('authors.json', authors)
    print("Скрапінг завершено. Дані збережено у файли quotes.json та authors.json.")
