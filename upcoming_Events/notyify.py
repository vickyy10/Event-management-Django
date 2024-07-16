from twilio.rest import Client
from django.conf import settings

def send_whatsapp_message(to_number, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            from_=f'whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}',
            body=message,
            to=f'whatsapp:{to_number}'
        )
        print(f"WhatsApp message sent successfully! SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Failed to send WhatsApp message. Error: {str(e)}")
        return False
