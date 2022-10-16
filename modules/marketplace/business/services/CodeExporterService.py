import abc


class CodeExportService(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_
    """

    @abc.abstractmethod
    def __init__(self, serviceclass: object, utils: object) -> None:
        self.serviceclass = serviceclass
        self.utils = utils.get_utils()

    @abc.abstractmethod
    def export_module(self):
        """_summary_"""
        return

    @abc.abstractmethod
    def export_validators(self):
        """_summary_"""
        return

    @abc.abstractmethod
    def export_utils(self):
        """_summary_"""
        return

    @abc.abstractmethod
    def export_app(self):
        """_summary_"""
        return

    @abc.abstractmethod
    def export_boilerplate(self):
        """_summary_"""
        return

    @abc.abstractmethod
    def export_frontend(self, framework: str):
        """_summary_"""
        return

    @abc.abstractmethod
    def create_dockerfiles(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def add_wsgi_server(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def export_with_cython_build(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def api_app_exporter(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def frontend_app_exporter(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def export_android_build_apk(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def export_android_build_aab(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def export_ios_app_xcode_project(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def export_macos_app_xcode(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def export_winos_app(self, context):
        """_summary_

        Args:
            context (_type_): _description_
        """
        return

    @abc.abstractmethod
    def export_linux_app(self, context):
        """
        Args:
            context (_type_): _description_
        """
        return
