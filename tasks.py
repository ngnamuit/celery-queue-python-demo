from celery_worker import app as app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def delay(task, *args, **kwargs):
    """
    We dont use the original celery delay() because it can't specific running options.
    This function replaces the excrescence to enqueue task with apply_async
    task.apply_async(args=[...], kwargs={...}, task_id=..., countdown=...)
    See more here https://docs.celeryproject.org/en/latest/userguide/canvas.html#partials
    """
    def actually_send(**options):
        return task.s(*args, **kwargs).apply_async(**options)
    return actually_send

def send_mail(to_email, subject, html_content):
    message = Mail(
        from_email   = 'ngnamuit@gmai.com',
        to_emails    = to_email,
        subject      = subject,
        html_content = html_content
    )
    try:
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        return response
    except Exception as e:
        print(e.message)
@app.task
def send_mail_task(to_email, subject, html_content):
    send_mail(to_email, subject, html_content)

@app.task()
def add(x):
    import time
    time.sleep(1)
    return x + 1
