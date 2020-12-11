from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = [
        "get",
    ]

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        admin_id = 1
        queryset = User.objects.all().exclude(id=admin_id)
        return queryset
