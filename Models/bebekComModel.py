from typing import NamedTuple

#Bebek entitiyleri
class BebekAnswer(NamedTuple):
    name: str 
    date: str 
    comment: str  

class BebekComment(NamedTuple):
    name: str 
    date: str 
    comment: str 
    bebekAnswer: BebekAnswer
