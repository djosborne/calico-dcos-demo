import sys
from flask import Flask
import redis
import socket

REDIS_SERVER = sys.argv[1]

print("Using %s" % REDIS_SERVER)

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
	rc = redis.Redis(host=REDIS_SERVER, port=6379, db=0)

	raw_views = rc.incr('views')
	if raw_views == None:
		views = 1
	else:
		views = int(raw_views) + 1
	rc.set('views', str(views))

	return "%s views! Reporting from task %s on host %s" % (views, os.getenv('MESOS_TASK_ID'), socket.gethostname())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
