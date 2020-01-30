from celery.task import Task
from time import sleep

class CourseTask(Task):
    def __init__(self):
        self.name = 'course-task'

    def run(self, *args, **kwargs):
        print('start course task')
        sleep(4)
        print('args={}, kwargs={}'.format(args, kwargs))
        print('end course task')