import requests
from bs4 import BeautifulSoup
from typing import List
from Models.bebekComModel import BebekComment
import re

def BebekCom(url: str) -> List[BebekComment]:
    if not re.match(r'^https?:\/\/', url) and not url.startswith("javascript:"):
        raise ValueError("Geçersiz URL formatı")
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    commentsList = soup.find("div", id="comments")
    if not commentsList:
        return []

    commentsContainer = commentsList.find("div", class_="comments-container")
    commentsUl = commentsContainer.find("ul", class_="comment-list")
    if not commentsUl:
        return []

    def parse_comment(commentLi):
        commentArticle = commentLi.find("article")
        if not commentArticle:
            return []
        commentName = commentArticle.find("b").get_text(strip=True)
        commentDate = commentArticle.find("time").get_text(strip=True)
        commentParagraph = commentArticle.find("p").get_text(strip=True)

        # Yorumun alt yorumlarını bulan kısım
        repliesUl = commentLi.find("ul", class_="children")
        replies = []
        if repliesUl:
            repliesLi = repliesUl.find_all("li", recursive=False)
            for reply_li in repliesLi:
                replies.append(parse_comment(reply_li))

        return BebekComment(commentName, commentDate, commentParagraph, replies)

    commentsLi = commentsUl.find_all("li", recursive=False)
    bebekComments = []

    for commentLi in commentsLi:
        bebekComments.append(parse_comment(commentLi))

    return bebekComments

# bu classda çalışrtımka için
# url = "https://www.bebek.com/10-11-aylik-bebek-beslenmesi/"
# comments = BebekCom(url)
# for comment in comments:
#     print(comment,"\n")
