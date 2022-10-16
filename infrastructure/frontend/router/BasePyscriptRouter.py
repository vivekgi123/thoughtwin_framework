class BaseScriptRouter:
    routes = {}
    templates = {}

    def template(name, templatefunction):
        """_summary_

        Args:
            name (_type_): _description_
            templatefunction (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.templates[name] = templatefunction
        return self.templates[name]

    def route(self, path, template):
        """_summary_

        Args:
            path (_type_): _description_
            template (_type_): _description_

        Returns:
            _type_: _description_
        """
        if isinstance(template, function) == True:
            self.routes[path] = template
            return self.routes[path]
        elif isinstance(template, str) == True:
            self.routes[path] = self.templates[template]
            return self.routes[path]
        else:
            return
