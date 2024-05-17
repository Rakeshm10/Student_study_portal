from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        if username == 'admin' and password == 'rakesh123':
            try:
                return User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        return None
