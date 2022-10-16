import importlib
import os
import json
from . import user_validator, user_log_validator


class GetValidator:
    def get_validator(self, modelname):
        with open(os.getenv("validatorconfig"), "rb") as fs:
            data = json.loads(fs.read())
            path = data.get(modelname)
            module = importlib.__import__("utilities")
            module = getattr(module, "validators")
            path = path.split(".")
            package = getattr(module, path[0])
            return getattr(package, path[1])
