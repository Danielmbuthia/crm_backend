from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reminder
from .tasks import schedule_reminder_tasks


@receiver(post_save, sender=Reminder)
def handle_reminder_save(sender, instance, created, **kwargs):
    if created:
        schedule_reminder_tasks(instance.id)
    else:
        schedule_reminder_tasks(instance.id)
