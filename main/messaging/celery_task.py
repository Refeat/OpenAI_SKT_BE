from celery import Celery
import time
from drafts.models import *

app = Celery("tasks", broker="pyamqp://guest@192.168.0.70//")


@app.task
def add(x, y):
    time.sleep(3)
    pj = Project.objects.all()
    print(pj)
    print("hwello!!", x + y)
    return x + y


# if __name__ == "__main__":
#     add.delay(1, 3)
