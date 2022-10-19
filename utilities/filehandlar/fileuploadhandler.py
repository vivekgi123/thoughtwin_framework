from pyparsing import Dict, Optional
import requests
from typing import Optional,Dict
import base64

class Fileupload:
    def get_file(self,path:str,method:Optional[str]=None,config:Optional[Dict[str,str]]=None):
        """_summary_

        Args:
            path (str): _description_
            method (Optional[str], optional): _description_. Defaults to None.
            config (Optional[Dict[str,str]], optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if path.startswith("http") or path.startswith("https"):
            if config is not None:
                file=getattr(requests,method)(**config)
            else:
                file=getattr(requests,method)(path)

        
        with open(path,'rb') as fs:
            file=fs.read()
        convert=base64.b64encode(file)
        return convert

            
        


