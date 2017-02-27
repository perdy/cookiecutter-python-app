from {{ cookiecutter.app_slug }}.base_app import BaseApp


class App(BaseApp):
    def run(self, *args, **kwargs):
        pass
