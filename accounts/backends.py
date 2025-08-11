from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    """Authenticate using either username or email address."""
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('username_or_email') or kwargs.get('email') or kwargs.get('username')
        try:
            # try by username first (fast) then by email
            user = None
            if username and UserModel.objects.filter(username=username).exists():
                user = UserModel.objects.get(username=username)
            elif username and "@" in username and UserModel.objects.filter(email__iexact=username).exists():
                user = UserModel.objects.get(email__iexact=username)
        except UserModel.DoesNotExist:
            return None

        if user is None:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
