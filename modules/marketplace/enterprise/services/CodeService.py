from modules.marketplace.business.services.CodeExporterService import CodeExportService


class CodeExporterServices(CodeExportService):
    """_summary_

    Args:
        CodeExportService (_type_): _description_
    """

    def __init__(self, serviceclass: object, utils: object) -> None:
        """_summary_

        Args:
            serviceclass (object): _description_
            utils (object): _description_
        """
        super().__init__(serviceclass, utils)

    def export_app(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().export_app()

    def export_boilerplate(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().export_boilerplate()

    def export_module(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().export_module()

    def export_utils(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().export_utils()

    def export_validators(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().export_validators()

    def export_frontend(self, framework: str):
        """_summary_

        Args:
            framework (str): _description_

        Returns:
            _type_: _description_
        """
        return super().export_frontend(framework)

    def export_android_build_aab(self, context):
        """_summary_

        Args:
            context (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().export_android_build_aab(context)

    def export_android_build_apk(self, context):
        """_summary_

        Args:
            context (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().export_android_build_apk(context)

    def export_ios_app_xcode_project(self, context):
        """_summary_

        Args:
            context (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().export_ios_app_xcode_project(context)

    def export_macos_app_xcode(self, context):
        """_summary_

        Args:
            context (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().export_macos_app_xcode(context)

    def export_winos_app(self, context):
        """_summary_

        Args:
            context (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().export_winos_app(context)

    def export_linux_app(self, context):
        """_summary_

        Args:
            context (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().export_linux_app(context)
