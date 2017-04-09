from flask import Flask
from flask import request
import logging

app = Flask(__name__)
log = logging.getLogger(__name__)


@app.route('/calculate')
def calculate():
    try:
        x = request.args.get("x")
        result = 1/(1-float(x))
        return str(result)
    except ZeroDivisionError:
        return "undefined"
    except Exception as e:
        log.error(str(e))
        return "invalid input"
