import abc
from typing import Optional
from modules.user_activity_module.business.services.User_log_service import (
    Userlogservice,
)


class UserLogServices(Userlogservice):
    """_summary_

    Args:
        abc (_type_): _description_

    Returns:
        _type_: _description_
    """

    def __init__(self, dbmanager: object, model: Optional[object] = None) -> None:
        """_summary_

        Args:
            dbmanager (object): _description_
            model (Optional[object], optional): _description_. Defaults to None.
        """
        super().__init__(dbmanager, model)

    def create(self, data: dict):
        """_summary_

        Args:
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().create(data)

    def update(self, model: object, key: dict, data: dict):
        """_summary_

        Args:
            key (dict): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().update(model, key, data)

    def delete(self, model: object, key: dict):
        return super().delete(model, key)

    def get(self, model: object, key: dict):
        """_summary_

        Args:
            key (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().get(model, key)

    def get_all(self, model: object):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().get_all(model)
