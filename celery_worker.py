from celery import Celery
import logging
import celeryconfig
import time
logger = logging.getLogger(__name__)
import json

config_file = 'config.test.json'
config      = {}
with open(config_file) as config_file:
    config = json.load(config_file)

app = Celery('celery_worker', broker=config['broker_url'],  backend=config['backend_url'])
app.config_from_object(celeryconfig)


@app.task()
def sum(x, y):
    time.sleep(2)
    return x + y
if __name__ == '__main__':
    logger.info("WORKERS IS STARTING")
    app.worker_main()
