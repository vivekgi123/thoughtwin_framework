"""primission model"""
import datetime
from email.policy import default
from redis_om import HashModel, Field
from typing import Optional


class Permission(HashModel):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    permissionname: str = Field(index=True)
    permissionview: str = Field(index=True)
    created_at: datetime.datetime = Field(index=True, default=datetime.datetime.today())
    updated_at: Optional[datetime.datetime] = None
