from flask import Flask
from flask import request

import config
from config import LOG_FILE

import logging

app = Flask(__name__)
app.config.from_object(config)

#LOGGING_CONFIG = {
#    'version': 1, # required
#    'disable_existing_loggers': True, # this config overrides all other loggers
#    'formatters': {
#        'precise': {
#            'format': '%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s',
#            'datefmt': '%Y-%m-%d %H:%M:%S'
#        }
#    },
#    'handlers': {
#        'default': {
#            'level': 'INFO',
#            'formatter': 'precise',
#            'class': 'logging.StreamHandler',
#        },
#        'file': {
#            'class' : 'logging.handlers.RotatingFileHandler',
#            'formatter': 'precise',
#            'filename': LOG_FILE,
#            'maxBytes': '1024',
#            'backupCount': '3',
#            'level': 'DEBUG',
#        }
#    },
#    'loggers': {
#        '': {
#            'handlers': ['default'],
#            'level': 'INFO',
#            'propagate': True
#        },
#        __name__: {
#            'level': 'DEBUG',
#            'handlers': ['file'],
#            'propagate': False
#        }
#    }
#}
#
#logging.config.dictConfig(LOGGING_CONFIG)
LOG = logging.getLogger(__name__)

@app.route('/calculate')
def calculate():
    try:
        x = request.args.get("x")
        result = 1/(1-float(x))
        return str(result)
    except ZeroDivisionError:
        return "undefined"
    except Exception as exc:
        LOG.exception(exc)
        return "invalid input"
