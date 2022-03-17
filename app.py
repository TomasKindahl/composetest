import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def fullhtml(title, content):
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "  <head>\n"
    S += "    <meta charset='utf-8'/>\n"
    S += "    <title>{}</title>\n".format(title)
    S += "  </head>\n"
    S += "  <body>\n"
    S += "    <h1>{}</h1>\n".format(title)
    S += "    {}\n".format(content)
    S += "  </body>\n"
    S += "</html>\n"
    return S

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Guten Tag Welt! Ich bin {} Weile gesehen.\n'.format(count)

@app.route('/ykk')
def ykk():
    return fullhtml("Ykk!","<p>Ykk!</p>")
