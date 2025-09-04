from pydantic import BaseModel
from typing import List,Optional

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None

Comment.model_rebuild()

comment=Comment(
    id=1,
    content='bhgiedfhguefgb',
    replies=[
        Comment(
            id=1,
            content='bhgiedfhguefgb',
            replies=[
                Comment(
            id=1,
            content='bhgiedfhguefgb'
        )
            ]
        )
    ]
)