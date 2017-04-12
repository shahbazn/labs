import logging
import logging.config


from .app import app
from config import LOG_FILE


LOGGING_CONFIG = {
    'version': 1, # required
    'disable_existing_loggers': True, # this config overrides all other loggers
    'formatters': {
        'precise': {
            'format': '%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'default': { 
            'level': 'INFO',
            'formatter': 'precise',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class' : 'logging.handlers.RotatingFileHandler',
            'formatter': 'precise',
            'filename': LOG_FILE,
            'maxBytes': '1024',
            'backupCount': '3',
            'level': 'DEBUG',
        }
    },
    'loggers': {
        '': { 
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        __name__: {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
