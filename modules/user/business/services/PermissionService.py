import abc
from ast import Delete
from typing import Optional


class PermissionService(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_

    Returns:
        _type_: _description_
    """

    @abc.abstractmethod
    def __init__(self, dbmanager: object, model: Optional[object] = None) -> None:
        self.dbmanager = dbmanager
        self.model = model

    @abc.abstractmethod
    def create(self, data: dict):
        """_summary_

        Args:
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        for k, v in data.items():
            setattr(self.model, k, v)
        return self.dbmanager.create(self.model)

    @abc.abstractmethod
    def get(self, key: dict):
        """_summary_

        Args:
            key (dict): _description_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.get(self.model, key)

    @abc.abstractmethod
    def get_all(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.get_all(self.model)

    @abc.abstractmethod
    def update(self, key: dict, data: dict):
        """_summary_

        Args:
            key (dict): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.update(key, data, self.model)

    @abc.abstractmethod
    def delete(self, key: dict):
        """_summary_

        Args:
            key (dict): _description_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.delete(key, self.model)
