from .models import Address, Profile


def get_user_profile(user):
    return Profile.objects.filter(
        user=user,
        is_deleted=False,
    ).first()


def get_user_addresses(user):
    return Address.objects.filter(
        user=user,
        is_deleted=False,
    )


def get_default_address(user):
    return get_user_addresses(user).filter(is_default=True).first()