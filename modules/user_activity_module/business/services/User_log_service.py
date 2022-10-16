import abc
from typing import Optional


class Userlogservice(abc.ABC):
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
    def create(self, data: object):
        """_summary_

        Args:
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.create(data)

    @abc.abstractmethod
    def get(self, model: object, key: dict):
        """_summary_

        Args:
            key (dict): _description_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.get(model, key)

    @abc.abstractmethod
    def get_all(self, model: object):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.get_all(model)

    @abc.abstractmethod
    def update(self, model: object, key: dict, data: dict):
        """_summary_

        Args:
            key (dict): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.update(model, key, data)

    @abc.abstractmethod
    def delete(self, model, key: dict):
        """_summary_

        Args:
            key (dict): _description_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.delete(key, model)
