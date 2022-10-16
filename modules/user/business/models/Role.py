"""role model"""
from typing import List, Optional
import datetime
from redis_om import HashModel, Field


class Role(HashModel):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    rolename: str = Field(index=True)
    permissions: List[str] = Field(index=True)
    created_at: datetime.datetime = Field(index=True, default=datetime.datetime.today())
    updated_at: Optional[datetime.datetime] = None
