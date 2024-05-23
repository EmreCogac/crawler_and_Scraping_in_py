from dataclasses import dataclass, field
from typing import List

@dataclass
class BebekComment:
    name: str
    date: str
    comment: str
    replies: List['BebekComment'] = field(default_factory=list)
# Normal listeden iç içe recursive liste ile ağaç yapısı oluşturulup daha stabil bir yapı oluşturulmuştur

# from typing import NamedTuple

# #Bebek entitiyleri
# class BebekAnswer(NamedTuple):
#     name: str 
#     date: str 
#     comment: str  

# class BebekComment(NamedTuple):
#     name: str 
#     date: str 
#     comment: str 
#     bebekAnswer: BebekAnswer[0]
