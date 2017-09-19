# This file was adapted from the Docker sample posted with the 'Get started with Docker Compose' doc
#   URL:            https://docs.docker.com/compose/gettingstarted/#step-1-setup
#   Date accessed:  April 2017

from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)
redis = Redis(host='hello_db', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    container_id = socket.gethostname()
    container_ip = socket.gethostbyname(container_id)
    returnMe = '<!DOCTYPE html><html><head><title>Hello</title></head><body><h2>Hello world! This app has been accessed {} times.</h2>'.format(count)
    returnMe = returnMe+'<p><i>This request was handled by the following "web" container instance:</i></p>'
    returnMe = returnMe+'<p>Container ID: '+container_id+'<br>'
    returnMe = returnMe+'Container IP: '+container_ip+'</p></body></html>'
    return returnMe

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
