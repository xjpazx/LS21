from celery import current_app as app


@app.task()
def task_test():
    print('Hello Celery')
