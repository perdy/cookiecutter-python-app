import logging
from argparse import ArgumentParser

from {{cookiecutter.project_slug}} import __description__


class App:
    def __init__(self):
        self.args = self.parse_args()
        self.logger = self.get_logger()

    def get_logger(self):
        return logging.getLogger(__name__)

    def parse_args(self):
        parser = ArgumentParser(description=__description__)

        parser.add_argument('args', help='positional args')

        return parser.parse_args()

    def run(self):
        pass
