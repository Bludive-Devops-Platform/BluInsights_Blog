from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BlogCreate(BaseModel):
    title: str
    content: str
    tags: Optional[str]
    author: Optional[str]
    image_url: Optional[str]

class BlogUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    tags: Optional[str]
    image_url: Optional[str]

    class Config:
        from_attributes = True

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    tags: Optional[str]
    author: Optional[str]
    image_url: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
