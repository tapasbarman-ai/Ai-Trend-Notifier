from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_admin: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Subscriber Schemas
class SubscriberBase(BaseModel):
    email: EmailStr

class SubscriberCreate(SubscriberBase):
    pass

class Subscriber(SubscriberBase):
    id: int
    subscribed_at: datetime
    is_active: bool

    class Config:
        from_attributes = True

# Newsletter Schemas
class NewsletterBase(BaseModel):
    title: str
    summary: str
    content: str
    sentiment: str

class NewsletterCreate(NewsletterBase):
    pass

class Newsletter(NewsletterBase):
    id: int
    published_at: datetime

    class Config:
        from_attributes = True
