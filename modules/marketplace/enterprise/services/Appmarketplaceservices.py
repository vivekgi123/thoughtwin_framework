from modules.marketplace.business.services.Appmarketplaceservice import Appmarketplace


class Appmarketplaceservice(Appmarketplace):
    """_summary_

    Args:
        Appmarketplace (_type_): _description_
    """

    def __init__(self, dbmanager: object, utils: object) -> None:
        """_summary_

        Args:
            dbmanager (object): _description_
            utils (object): _description_
        """
        super().__init__(dbmanager, utils)

    def create(self, model: object):
        """_summary_

        Args:
            model (object): _description_

        Returns:
            _type_: _description_
        """
        return super().create(model)

    def get(self, model: object, key: dict):
        """_summary_

        Args:
            model (object): _description_
            key (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().get(model, key)

    def get_all(self, model: object):
        """_summary_

        Args:
            model (object): _description_

        Returns:
            _type_: _description_
        """
        return super().get_all(model)

    def update(self, model: object, key: dict, data: dict):
        """_summary_

        Args:
            model (object): _description_
            key (dict): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().update(model, key, data)

    def delete(self, model: object, key: dict):
        """_summary_

        Args:
            model (object): _description_
            key (dict): _description_

        Returns:
            _type_: _description_
        """
        return super().delete(model, key)
