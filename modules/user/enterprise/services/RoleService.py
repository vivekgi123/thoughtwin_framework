import abc
from typing import Optional
from modules.user.business.services.RoleService import RoleService


class RoleServices(RoleService):
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

    def update(self, key: dict, data: dict):
        """_summary_

        Args:
            key (dict): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().update(key, data)

    def get(self, key: dict):
        """_summary_

        Args:
            key (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().get(key)

    def get_all(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().get_all()

    def delete(self, key: dict):
        """_summary_

        Args:
            key (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().delete(key)
