import time
import pandas as pd
import requests
from datetime import timedelta 
from bs4 import BeautifulSoup
from transform import transform_data, transform_to_DataFrame  # Mengimpor fungsi dari modul transform
from load import export_to_csv # Mengimpor fungsi dari modul load
from prefect import task, flow
 
 
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

@task(name="Fetching Content", retries=3, retry_delay_seconds=5)
def fetching_content(url: str):
    """Mengambil konten HTML dari URL yang diberikan."""
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")

@task(name="Extract Book Data")
def extract_book_data(article: BeautifulSoup):
    """Mengambil data buku berupa judul, harga, ketersediaan, dan rating dari article (element html)."""
    book_title = article.find("h3").find("a").get("title")
    product_element = article.find('div', class_='product_price')
    price = product_element.find('p', class_='price_color').text
    availability_element = product_element.find('p', class_='instock availability')
    available = "Available" if availability_element else "Not Available"

    rating_element = article.find('p', class_='star-rating')
    rating = rating_element['class'][1] if rating_element else "Rating not found"

    books = {
        "Title": book_title,
        "Price": price,
        "Availability": available,
        "Rating": rating
    }

    return books

@flow(name="Scraping Book Data")
def scrape_book(base_url: str, max_page: int = 10, delay: int = 2):
    """Fungsi utama untuk mengambil keseluruhan data, mulai dari requests hingga menyimpannya dalam variabel data."""
    data = []
    page_number = 1

    for i in range(1, max_page + 1):
        url = base_url.format(page_number)
        print(f"Scraping halaman: {url}")

        content = fetching_content(url)
        if content:
            soup = BeautifulSoup(content, "html.parser")
            articles_element = soup.find_all('article', class_='product_pod')
            for article in articles_element:
                book = extract_book_data(article)
                data.append(book)

            next_button = soup.find('li', class_='next')
            if next_button:
                page_number += 1
                time.sleep(delay) # Delay sebelum halaman berikutnya

                if page_number == 5: # For hands-on purposes
                    break # Berhenti jika sudah mencapai halaman 5
            else:
                break # Berhenti jika sudah tidak ada next button
        else:
            break # Berhenti jika ada kesalahan

    return data

@flow(name="Main Flow")
def main(base_url: str = 'https://books.toscrape.com/catalogue/page-{}.html', 
    max_pages: int = 5, 
    delay: int = 2): # Menambahkan parameter
    
    """Fungsi utama untuk keseluruhan proses scraping hingga menyimpannya."""
    all_books_data = scrape_book(base_url, max_pages, delay)
    if all_books_data:
        df = transform_to_DataFrame(all_books_data)   # Mengubah variabel all_books_data menjadi df.
        df = transform_data(df, 20000)   # Mentransformasikan data
        export_to_csv(df, "product")
    else:
        print("Tidak ada data yang ditemukan.")
 
 
if __name__ == '__main__':
    main.serve(
        name="daily-website-scraper",
        tags=["scraping", "books"],
        parameters={"base_url": "https://books.toscrape.com/catalogue/page-{}.html", "max_pages": 5},
        interval=timedelta(days=1),
        pause_on_shutdown=False
        # Alternatif menggunakan Cron (misal setiap jam 2 pagi):
        # cron="0 2 * * *" 
    )