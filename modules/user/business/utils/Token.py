from datetime import datetime
from typing import Optional
import jwt
import datetime
import os


class Token:
    """_summary_"""

    def generate(self, payload):
        """_summary_

        Args:
            payload (_type_): _description_
        """
        payload.update({"exp": datetime.datetime.today() + datetime.timedelta(days=7)})
        encoded_access = jwt.encode(payload, os.getenv("secret_key"), algorithm="HS256")
        payload.update({"exp": datetime.datetime.today() + datetime.timedelta(days=15)})
        encoded_refresh = jwt.encode(
            payload, os.getenv("secret_key"), algorithm="HS256"
        )
        return dict(access_token=encoded_access, refresh_token=encoded_refresh)

    def decode(self, token):
        """_summary_

        Args:
            token (_type_): _description_
        """
        return jwt.decode(token, os.getenv("secret_key"), algorithms=["HS256"])

    def from_refresh(self, token):
        """_summary_

        Args:
            token (_type_): _description_
        """
        payload = self.decode(token)
        return self.generate(payload)
