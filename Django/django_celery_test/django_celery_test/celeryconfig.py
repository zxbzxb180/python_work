import djcelery
djcelery.setup_loader()

BROKER_BACKEND = 'redis'
BROKER_URL = 'redis://:6222580@localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://:6222580@localhost:6379/2'

CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue'
    }
}

CELERY_DEFAULT_QUEUE = 'work_queue'


CELERY_IMPORTS = (
    'course.tasks',

)

#有些情况防止死锁
CELERYD_FORCE_EXECV = True

#设置并发的worker数量
CELERYD_CONCURRENCY = 4

#允许重试
CELERY_ACKS_LATE = True

#每个worker最多执行100个任务，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100

#单个任务最大执行时间
CELERYD_TASK_TIME_LIMIT = 12 * 30
