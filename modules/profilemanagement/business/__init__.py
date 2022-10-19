from typing import List,Optional
import importlib
import os
from . import *
class UserModelIdentifier:
    @classmethod
    def get_user_model(cls):
        user=importlib.__import__('modules')
        path=os.getenv('user_model_path')
        path=path.split(".")
        user=[getattr(user,x) for x in path][0]
        return user
