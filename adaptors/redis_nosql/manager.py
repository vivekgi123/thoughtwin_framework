import asyncio
from datetime import datetime
import json
from typing import Dict, Optional, List, Any
from wsgiref.validate import validator


class DataBaseManager:
    """_summary_"""

    def __init__(
        self, db_object: object, db_settings: object, validators: object
    ) -> None:
        self.validators = validators
        self.db_object = db_object
        self.db_settings = db_settings
        self.connect()

    def connect(self):
        """_summary_"""
        return self.db_settings().run()

    def create(self, model: object):
        """_summary_

        Args:
            model (object): _description_
        """
        validator = self.validators.get_validator(model.__class__.__name__)
        validated_model = validator().validate_data(model)
        return validated_model.save()

    def get(self, model: object, key: Optional[Any] = None):
        """_summary_

        Args:
            model (object): _description_
            key (Optional[Any], optional): _description_. Defaults to None.
        """
        try:
            data = model.get(
                getattr(model, list(key.keys())[0]) == list(key.values())[0]
            )
        except Exception as e:
            data = e
        return data

    def get_all(self, model: object):
        """_summary_

        Args:
            model (object): _description_
        """
        try:
            model.find(model.pk == "*").all()
        except Exception as e:
            return []

    def update(self, key: Dict, data: Dict, model: object):
        """_summary_

        Args:
            key (Dict): _description_
            data (Dict): _description_
            model (object): _description_
        """
        obj = self.get(model, key=key)
        for k, v in data.items():
            setattr(obj, k, v)
        obj.updated_at = datetime.today()
        try:
            obj.save()
        except Exception as e:
            return e
        return obj

    def delete(self, key: Dict, model: object):
        """_summary_

        Args:
            key (Dict): _description_
            model (object): _description_
        """
        obj = self.get(model, key=key)
        try:
            obj.delete()
        except Exception as e:
            return e
        return obj
