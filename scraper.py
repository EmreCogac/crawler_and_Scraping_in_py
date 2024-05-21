import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.bebek.com/bebeginizin-cinsiyetini-belirleyebilir-misiniz/')
soup = BeautifulSoup(page.text, 'html.parser')

# artist_name_list = soup.find("div", id="comments")
# deneme = artist_name_list.find("div", class_= "comments-container")
# deneme1 = deneme.find("ul", class_="comment-list")
# deneme2 = deneme1.find("li", id = "comment-62914")
# deneme3 = deneme2.find("p")
artist_name_list = soup.find("div", id="comments")
deneme = artist_name_list.find("div", class_= "comments-container")
deneme1 = deneme.find("ul", class_="comment-list")
deneme2 = deneme1.find_all("li")
for elemet in deneme2:
    deneme3  = elemet.find_all("article")
    for p in deneme3:
        a = p.find("p")
        print(a)

# artist_name_list_items = artist_name_list.find_all('div',class_='comment-body')

# for artist_name in artist_name_list_items:
#     print(artist_name.prettify())