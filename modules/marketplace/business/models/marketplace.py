from datetime import datetime
from typing import Dict, Optional
from redis_om import HashModel, Field


class Typeconfig(HashModel):
    """_summary_

    Args:
        HashModel (_type_): _description_
    """

    type_code: str
    config_data: Dict[str, str] = Field(index=True)


class Marketplace(HashModel):
    """_summary_

    Args:
        HashModel (_type_): _description_
    """

    app: Typeconfig
    modules: Typeconfig
    adapters: Typeconfig
    templates: Typeconfig
    created_at: datetime = Field(index=True, default=datetime.today())
    updated_at: Optional[datetime] = Field(index=True, default=datetime.today())
