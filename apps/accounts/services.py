from .models import Address, Profile


def get_or_create_profile(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    return profile


def update_profile(*, user, full_name=None, phone=None, avatar=None):
    profile = get_or_create_profile(user)

    if full_name is not None:
        profile.full_name = full_name

    if phone is not None:
        profile.phone = phone

    if avatar is not None:
        profile.avatar = avatar

    profile.save()
    return profile


def set_default_address(*, user, address):
    Address.objects.filter(user=user, is_default=True).update(is_default=False)

    address.is_default = True
    address.save(update_fields=["is_default", "updated_at"])
    return address


def delete_address(address):
    address.soft_delete()
    return address