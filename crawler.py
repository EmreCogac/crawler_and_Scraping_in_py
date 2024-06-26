import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from Scrapers.bebekScraper import BebekCom
from Scrapers.bebekForumScraper import BebekForum
# Website buraya gelir
# burası bir fonksiyon olacak
# bu fonksiyon dönüt olarak json dönecek
# her scraper için ayrı bir scraper fonksiyonu yazılacak
# bunların türlerine göre scrapera yönlendiricek 
# scraperdan bir json alacak 
# bu jsonu döndürecek
# kadınlar klubü anneler kukubü
# 
base_url =  "https://forum.bebek.com"

visited_urls = set()

urls_to_visit = [base_url]

# Keşfedilmişleri kuyruğa alır 

def crawl_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # http statusleri alır 200, 500
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Kuyruğa yeni bağlantılar ekler
        comments = []
        links = []
        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            links.append(next_url)
        
        return links
    except requests.exceptions.RequestException as e:
        print(f"HAta  {url}: {e}")
        return []
# websiteyi gezer
while urls_to_visit:
    current_url = urls_to_visit.pop(0)  # ilk url çıkartır
    if current_url in visited_urls:
        continue
    if current_url.startswith(base_url) and '#' not in current_url and "?" not in current_url:
        print(f"Crawling: {current_url}")
        scrapedStruct = BebekForum(current_url)
        print(scrapedStruct ,"\n")
        new_links = crawl_page(current_url)
        visited_urls.add(current_url)
        urls_to_visit.extend(new_links)
print("Crawling biti.")