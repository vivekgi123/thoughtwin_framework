import abc
from typing import Optional

import abc
from typing import Optional
from modules.user.business.services.UserSessionService import UserSessionService


class UserServices(UserSessionService):
    """_summary_

    Args:
        abc (_type_): _description_

    Returns:
        _type_: _description_
    """

    def __init__(
        self, dbmanager: object, token: object, model: Optional[object] = None
    ) -> None:
        """_summary_

        Args:
            dbmanager (object): _description_
            token (object): _description_
            model (Optional[object], optional): _description_. Defaults to None.
        """
        super().__init__(dbmanager, token, model)

    def get_token(self, payload: dict):
        """_summary_

        Args:
            payload (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().get_token(payload)

    def decode_token(self, token: str):
        """_summary_

        Args:
            token (str): _description_

        Returns:
            _type_: _description_
        """
        return super().decode_token(token)

    def claim_from_refresh_token(self, token: str):
        """_summary_

        Args:
            token (str): _description_

        Returns:
            _type_: _description_
        """
        return super().claim_from_refresh_token(token)
