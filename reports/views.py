from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    http_method_names = [
        "get",
    ]

    def get_queryset(self):
        queryset = Report.objects.all()
        user_id = self.request.query_params.get("user_id", None)
        if user_id is not None:
            queryset = queryset.filter(
                Q(author_id=user_id) | Q(responses__author_id=user_id)
            )
        return queryset
