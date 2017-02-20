import logging
import logging.config
from abc import abstractmethod, ABCMeta
from argparse import ArgumentParser


class BaseApp(metaclass=ABCMeta):
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'brief': {
                'format': '[%(levelname)s] %(message)s'
            },
            'default': {
                'datefmt': '%Y-%m-%d %H:%M:%S',
                'format': '"[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'brief',
                'level': 'DEBUG',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'default'
            }
        },
        'loggers': {
            '{{cookiecutter.app_slug}}': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    }

    def __init__(self):
        self.args = self.parse_args()
        self.logger = self.get_logger()

    def get_logger(self):
        logging.config.dictConfig(self.LOGGING_CONFIG)

        return logging.getLogger(__name__)

    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*', default=[], help='positional args')

    def parse_args(self):
        parser = ArgumentParser(
            description='{{cookiecutter.project_short_description}}'
        )

        self.add_arguments(parser)

        return vars(parser.parse_args()

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
