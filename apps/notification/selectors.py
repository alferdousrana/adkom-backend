from .models import Notification


def get_user_notifications(user):
    return Notification.objects.filter(
        user=user,
        is_deleted=False,
    )


def get_unread_notifications(user):
    return get_user_notifications(user).filter(is_read=False)


def get_read_notifications(user):
    return get_user_notifications(user).filter(is_read=True)


def get_notification_count(user):
    return get_user_notifications(user).count()


def get_unread_notification_count(user):
    return get_unread_notifications(user).count()