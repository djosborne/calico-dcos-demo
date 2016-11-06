import sys
import os
from flask import Flask
import redis
import socket

REDIS_SERVER = sys.argv[1]

print("Using %s" % REDIS_SERVER)

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
	rc = redis.Redis(host=REDIS_SERVER, port=6379, db=0)

	views = rc.incr('views')

	return "%s views! Reporting from executor %s on host %s" % (views, os.getenv('MESOS_EXECUTOR_ID'), os.getenv('HOST'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
