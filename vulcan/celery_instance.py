from celery import Celery

import vulcan.celery_config as celery_config
celery_app = Celery('celery_test', backend='redis://localhost', broker='redis://localhost')
celery_app.config_from_object(celery_config)
celery_app.autodiscover_tasks(['project.services.project_tasks', 'user.services.user_tasks'], force=True)


@celery_app.task
def test_celery():
    print(4)
