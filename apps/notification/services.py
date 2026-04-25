from django.utils import timezone

from .models import Notification


def create_notification(*, user, title, message, data=None):
    return Notification.objects.create(
        user=user,
        title=title,
        message=message,
        data=data or {},
    )


def mark_notification_as_read(notification):
    if notification.is_read:
        return notification

    notification.is_read = True
    notification.read_at = timezone.now()
    notification.save(update_fields=["is_read", "read_at", "updated_at"])
    return notification


def mark_notification_as_unread(notification):
    if not notification.is_read:
        return notification

    notification.is_read = False
    notification.read_at = None
    notification.save(update_fields=["is_read", "read_at", "updated_at"])
    return notification


def mark_all_notifications_as_read(user):
    return Notification.objects.filter(
        user=user,
        is_read=False,
        is_deleted=False,
    ).update(
        is_read=True,
        read_at=timezone.now(),
    )


def delete_notification(notification):
    notification.soft_delete()
    return notification