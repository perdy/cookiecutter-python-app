import sys

from {{ cookiecutter.app_slug }}.app import App


if __name__ == '__main__':
    sys.exit(App().run())
