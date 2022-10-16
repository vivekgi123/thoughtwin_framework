import abc


class Appmarketplace(abc.ABC):
    @abc.abstractmethod
    def __init__(self, dbmanager: object, utils: object) -> None:
        self.dbmanager = dbmanager
        self.utils = utils.get_utils()
        self.validator = self.utils.validator

    @abc.abstractmethod
    def create(self, model: object):
        """_summary_

        Args:
            model (object): _description_
        """
        return self.dbmanager.create(model)

    @abc.abstractmethod
    def get(self, model: object, key: dict):
        """_summary_

        Args:
            model (object): _description_
            key (dict): _description_
        """
        return self.dbmanager.get(model, key)

    @abc.abstractmethod
    def get_all(self, model: object):
        """_summary_

        Args:
            model (object): _description_
        """
        return self.dbmanager.get_all(model)

    @abc.abstractmethod
    def update(self, model: object, key: dict, data: dict):
        """_summary_

        Args:
            model (object): _description_
            key (dict): _description_
            data (dict): _description_
        """
        return self.dbmanager.update(model, key, data)

    @abc.abstractmethod
    def delete(self, model: object, key: dict):
        """_summary_

        Args:
            model (object): _description_
            key (dict): _description_
        """
        return self.dbmanager.delete(model, key)
