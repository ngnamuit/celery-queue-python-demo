import tasks
from datetime import datetime


today_str = datetime.now().strftime("%Y%m%d %H:%M:%S")
A = tasks.delay(tasks.add, x=1)(task_id = f'add_{today_str}')
sent_email = tasks.delay(
                tasks.send_mail_task,
                to_email     = 'example@gmail.com',
                subject      = 'Just for testing send email',
                html_content = '<p>DEMO</p>'
             )(task_id = f'send_mail_{today_str}')