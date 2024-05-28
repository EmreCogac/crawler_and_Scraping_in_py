import requests
from bs4 import BeautifulSoup
from typing import List
from Models.bebekForumModel import BebekForumComment
from Models.bebekForumModel import BebekForumModel
import re
# -> List[BebekForumModel]:
def BebekForum(url: str):
    if not re.match(r'^https?:\/\/', url) and not url.startswith("javascript:"):
        raise ValueError("Geçersiz URL formatı")
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    forumPage = soup.find("div", id="bbpress-forums")
    if not forumPage:
        return []
   
    forumLead = forumPage.find("ul", class_="bbp-lead-topic")
    if not forumLead:
        return []
    
    forumLeadContentHeader = forumLead.find("li", class_="bbp-header")
    if not forumLeadContentHeader:
        return []
    
    forumLeadContent = forumLead.find("li", class_="bbp-body") 
    forumLeadContentData = forumLeadContent.find("p").get_text(strip=True) # content data
    forumLeadHeader = forumLeadContentHeader.find("div", class_="bbp-topic-author")
    if not forumLeadHeader:
        return []
    
    forumHeader = forumPage.find("h1", class_="topic-title").get_text(strip=True) # header name 
    if not forumHeader:
        return []
    
    forumLeadContentHeader = forumLead.find("li", class_="bbp-header")
    if not forumLead:
        return []
    
    forumLeadContent = forumLead.find("li", class_="bbp-body") 
    forumLeadContentData = forumLeadContent.find("p").get_text(strip=True) # content data

    forumLeadHeader = forumLeadContentHeader.find("div", class_="bbp-topic-author")
    forumLeadHeaderData = forumLeadHeader.find("div", class_="right")
    forumLeadHeaderName = forumLeadHeaderData.find("a").get_text(strip=True) # Name

    forumLeadMeta = forumLeadHeaderData.find("div" ,class_="meta")
    forumLeadMetaIgnore = forumLeadMeta.find("span", class_= "role")
    forumLeadMetaIgnore.decompose()
    forumLeadDate = forumLeadMeta.find("span").get_text(strip=True) # date 

    BebekComments = []

    def parse_comment(forumDiv):
        forumAuthor = forumDiv.find("div", class_="bbp-reply-author")
        if not forumAuthor:
            return []
        forumContent = forumDiv.find("div", class_="bbp-reply-content")
        if not forumContent:
            return []
        forumAuthorNameContent = forumAuthor.find("div", class_="right")
        if not forumAuthorNameContent:
            return []
        forumAuthorName = forumAuthorNameContent.find("a").get_text(strip=True)
        forumMeta = forumAuthorNameContent.find("div" ,class_="meta")
        forumMetaIgnore = forumMeta.find("span", class_= "role")
        forumMetaIgnore.decompose()
        date = forumMeta.find("span").get_text(strip=True)
        forumContentData = forumContent.find_all("p")
        contentDatas = ""
        for conentData in forumContentData:
            contentDatas = contentDatas + conentData.get_text(strip=True)
        
        if forumAuthorName != None and date != None and contentDatas != None:
            return BebekForumComment(forumAuthorName, date,contentDatas)
    
    forumCommentsUl = forumPage.find("ul", class_="forums bbp-replies")
    
    if not forumCommentsUl:
        return BebekForumModel(forumHeader,forumLeadHeaderName,forumLeadContentData,forumLeadDate,BebekComments)
    
    forumLi = forumCommentsUl.find("li", class_="bbp-body")

    if not forumLi:
        return BebekForumModel(forumHeader,forumLeadHeaderName,forumLeadContentData,forumLeadDate,BebekComments)
    
    forumDiv = forumLi.find_all("div", recursive=False)

    for forumDivs in forumDiv:
        BebekComments.append(parse_comment(forumDivs))
        
    if BebekComments != []:
        return BebekForumModel(forumHeader,forumLeadHeaderName,forumLeadContentData,forumLeadDate,BebekComments)


# url = "https://forum.bebek.com/topic/gogus-ucu-yaralari-icin-ne-yapmaliyim"
# comments = BebekForum(url)
# for comment in comments:
#     print(comment,"\n")