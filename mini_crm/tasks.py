from celery import current_app
from celery.schedules import crontab
from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail
from .models import Reminder


def schedule_reminder_tasks(reminder_id):
    reminder = Reminder.objects.get(id=reminder_id)
    reminder_time = reminder.reminder_time
    time_difference = (reminder_time - timezone.now()).total_seconds()

    print(reminder_id)

    if time_difference > 0:
        task_name = f'reminder_{reminder_id}'
        if task_name in current_app.conf.beat_schedule:

            del current_app.conf.beat_schedule[task_name]

        current_app.conf.beat_schedule[task_name] = {
            'task': 'mini_crm.tasks.send_reminder_email',
            'schedule': time_difference,
            'args': (reminder.id,),
            'expires': reminder_time,  
        }
        

@shared_task
def send_reminder_email(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        send_mail(
            subject=f"Reminder for {reminder.lead.name}",
            message=reminder.message,
            from_email='no-reply@gmail.com',  
            recipient_list=[reminder.lead.email],
        )
        print(f"Email sent to {reminder.lead.email}")
    except Reminder.DoesNotExist:
        print(f"Reminder with id {reminder_id} does not exist.")
    except Exception as e:
        print(f"Failed to send email: {e}")
