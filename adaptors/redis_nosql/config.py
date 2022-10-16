from typing import Optional, List
import os


class Config:
    """_summary_

    Returns:
        _type_: _description_
    """

    host: Optional[str] = os.getenv("Host")
    port: Optional[str] = os.getenv("Port")
    username: Optional[str] = os.getenv("Username")
    password: Optional[str] = os.getenv("Password")
    driver: Optional[str] = os.getenv("Driver")
    database: Optional[str] = os.getenv("Database")

    def get_db_url(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.username == "" and self.password == "":
            return f"{self.driver}://{self.host}:{self.port}/{self.database}"
        else:
            return f"{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
