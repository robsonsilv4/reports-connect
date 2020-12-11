from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.viewsets import ModelViewSet

from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(ModelViewSet):
    serializer_class = ReportSerializer
    http_method_names = [
        "get",
    ]

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Report.objects.all()
        user_id = self.request.query_params.get("user_id", None)
        if user_id is not None:
            queryset = queryset.filter(
                Q(author_id=user_id) | Q(responses__author_id=user_id)
            )
        return queryset
