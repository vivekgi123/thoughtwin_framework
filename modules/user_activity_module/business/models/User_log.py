from typing import Optional, Dict
import datetime
from redis_om import HashModel, Field


class UserLog(HashModel):
    """_summary_

    Args:
        HashModel (_type_): _description_
    """

    data: Optional[str] = None
    created_by: str = Field(index=True)
    created_at: datetime.datetime = Field(index=True, default=datetime.datetime.today())
    updated_at: Optional[datetime.datetime] = Field(index=True)
