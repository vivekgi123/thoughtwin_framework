import datetime
from distutils.command.config import config
from email.policy import default
from typing import Dict, Optional
from wsgiref import validate
from attr import attr
from redis_om import HashModel, Field
from modules.profilemanagement.business import UserModelIdentifier
from utilities.filehandlar.fileuploadhandler import Fileupload
User=UserModelIdentifier.get_user_model()

class ProfileManagement(HashModel):
    user:User
    location: str = Field(index=True)
    gender: str  = Field(index=True)
    profile_pic:str=Field(index=True)
    config:Optional[Dict[str,str]]=Field(index=True,default=None)
    created_at: datetime.datetime = Field(index=True,default=datetime.datetime.today())
    updated_at: Optional[datetime.datetime] = Field(index=True)

    @attr.__setattr__("profile_pic")
    def prof(self):
        if self.config is not None:
            file=Fileupload().get_file(self.config.get("path"),method=self.config.get('method'),config=self.config)
        else:
            file=Fileupload().get_file(self.config.get("path"))
        return file

    




    

