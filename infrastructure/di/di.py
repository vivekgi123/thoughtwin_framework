from pinject import BindingSpec, new_object_graph
from adaptors.redis_nosql.wrapper import AdaptorWrapper
from adaptors.redis_nosql.config import Config
from utilities.validators import GetValidator
from adaptors.redis_nosql.manager import DataBaseManager
import utilities


class Utils:
    def get_utils(self):
        return utilities


class FrameworkObjectGraph(BindingSpec):
    """_summary_

    Args:
        BindingSpec (_type_): _description_
    """

    def configure(self, bind):
        """_summary_

        Args:
            bind (_type_): _description_
        """
        bind("db_object", to_instance=AdaptorWrapper.connetion_agent())
        bind("db_settings", to_instance=AdaptorWrapper.setting_agent())
        bind("dbmanager", to_class=DataBaseManager)
        bind("validators", to_class=GetValidator)
        bind("utils", to_class=Utils)


obj_graph = new_object_graph(binding_specs=[FrameworkObjectGraph()])
