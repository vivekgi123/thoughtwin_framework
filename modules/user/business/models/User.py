from email.policy import default
from typing import Optional
import datetime
from redis_om import HashModel,Field



class User(HashModel):
    first_name: str = Field(index=True)
    last_name: str  = Field(index=True)
    email: str = Field(index=True)
    password: str = Field(index=True)
    role: Optional[str] = Field(index=True)
    created_at: datetime.datetime = Field(index=True,default=datetime.datetime.today())
    updated_at: Optional[datetime.datetime] = Field(index=True)