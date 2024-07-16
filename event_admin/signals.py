
from home.models import ClientDetails
from upcoming_Events.smtp import send_email
from upcoming_Events.models import UpcomingEvents
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from threading import Thread 

@receiver(post_save,sender=UpcomingEvents)
def send_notification_on_new_event(sender, instance, **kwargs):
    event = instance
    subject = 'New Event Added: {}'.format(event.Event_name)
    message = 'A new event has been added. Check it out!'
    users = ClientDetails.objects.all()

    for user in users:
        email_thread = Thread(
            target=send_email, args=(subject, message, settings.EMAIL_HOST, [user.email])
        )
        email_thread.start()
        


