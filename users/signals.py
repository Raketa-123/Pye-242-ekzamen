from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from django.core.mail import send_mail

@receiver(signal=post_save, sender=User)
def post_registration(
    sender: User, instance: User, created: bool, **kwargs
):
    if instance.is_superuser:
        return
    
    if created:
        code = str(instance.activation_code)
        send_mail(
            subject="Активация аккаунта",
            message=f"Ваш код активации: {code}",
            from_email="no-reply@example.com",
            recipient_list=["user@example.com"],
            fail_silently=False,
        )