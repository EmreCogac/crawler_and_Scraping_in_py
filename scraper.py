import requests
from bs4 import BeautifulSoup
from Models.bebekComModel import BebekComment
from Models.bebekComModel import BebekAnswer
# url = "https://www.bebek.com/bebeginizin-cinsiyetini-belirleyebilir-misiniz/"

def BebekCom(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    bebekComment = BebekComment("","date","",BebekAnswer("","date",""))
    # artist_name_list = soup.find("div", id="comments")
    # deneme = artist_name_list.find("div", class_= "comments-container")
    # deneme1 = deneme.find("ul", class_="comment-list")
    # deneme2 = deneme1.find("li", id = "comment-62914")
    # deneme3 = deneme2.find("p")
    # # test 
    commentsList = soup.find("div", id="comments")
    if not commentsList:
        return bebekComment
    else:  
        commentsContainter = commentsList.find("div", class_= "comments-container")
        commentsUl = commentsContainter.find("ul", class_="comment-list")
        if not commentsUl:
            return bebekComment
        commentsLi = commentsUl.find_all("li")
        if not commentsLi:
            return bebekComment
        for commentLi in commentsLi:
            commentArticle = commentLi.find("article")
            commentsAnsersLi = commentLi.find_all("li")
            if not commentsAnsersLi:
                return bebekComment
            commentName = commentArticle.find("b")
            commentParagraph = commentArticle.find("p")
            # print(commentName)
            # print(commentParagraph)
            counter = 0
            for answer in commentsAnsersLi:
                counter=counter+1
                print("comment ", counter)
                answerArticle = answer.find("article")   
                answerName = answerArticle.find("b")   
                answerParagraph = answerArticle.find("p")
                # print(answerName)
                # print(answerParagraph)
                bebekComment = BebekComment(commentName,"date",commentParagraph,BebekAnswer(answerName,"date",answerParagraph))
        return bebekComment
    
        # artist_name_list_items = artist_name_list.find_all('div',class_='comment-body')
        # for artist_name in artist_name_list_items:
        #     print(artist_name.prettify())