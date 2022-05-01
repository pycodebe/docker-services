from faktory import Worker
from app.views import TaskView
from framework.settings.common import FAKTORY_URL

w = Worker(
    faktory= FAKTORY_URL, 
    queues=['default'], 
    use_threads=True,
    concurrency=1,
    labels=["default",])

tasks = [TaskView.run_a_task, ]

for task in tasks:
    w.register(task.__name__, task)

w.run()