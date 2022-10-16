import abc
from typing import Optional


class UserSessionService(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_

    Returns:
        _type_: _description_
    """

    @abc.abstractmethod
    def __init__(
        self, dbmanager: object, token: object, model: Optional[object] = None
    ) -> None:
        self.dbmanager = dbmanager
        self.model = model
        self.token = token

    @abc.abstractmethod
    def get_token(self, payload: dict):
        """_summary_

        Args:
            payload (dict): _description_

        Returns:
            _type_: _description_
        """
        return self.token.generate(payload)

    @abc.abstractmethod
    def decode_token(self, token: str):
        """_summary_

        Args:
            token (str): _description_

        Returns:
            _type_: _description_
        """
        return self.token.decode(token)

    @abc.abstractmethod
    def claim_from_refresh_token(self, token: str):
        """_summary_

        Args:
            token (str): _description_

        Returns:
            _type_: _description_
        """
        return self.token.from_refresh(token)
