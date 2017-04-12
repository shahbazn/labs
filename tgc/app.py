from flask import Flask
from flask import request

import config
import logging

app = Flask(__name__)
app.config.from_object(config)
LOG = logging.getLogger('tgc')
#LOG.basicConfig(format=app.config['LOG_FORMAT'], datefmt='%Y-%m-%d %H:%M:%S')

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
