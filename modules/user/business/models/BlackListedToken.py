import datetime
from email.policy import default
from redis_om import HashModel, Field
from typing import Optional


class BlacklistToken(HashModel):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    token: str = Field(index=True)
    created_at: datetime.datetime = Field(index=True, default=datetime.datetime.today())
    updated_at: Optional[datetime.datetime] = Field(index=True)
