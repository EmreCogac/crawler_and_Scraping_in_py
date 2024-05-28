from dataclasses import dataclass, field

@dataclass
class BebekForumComment:
    name: str
    date: str
    comment: str

@dataclass
class BebekForumModel:
    topic: str
    leadConentName: str
    leadContent: str
    leadContentDate : str
    commentsList : list[str]


    
# @dataclass
# class BebekForum:
#     id: int
#     name: str
#     topic : str
#     date: str
#     comment: str
#     parentId : int
#     replies: List['BebekForum'] = field(default_factory=list)
    # Konunun ana yorumu 
    # Yorumların alıntıları