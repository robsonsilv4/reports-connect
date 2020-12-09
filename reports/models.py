from django.conf import settings
from django.db import models


class Report(models.Model):
    message = models.TextField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="users",
        on_delete=models.CASCADE,
    )
    supervisors = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"Report {self.id} - {self.message}"


class ReportResponse(models.Model):
    message = models.TextField(max_length=255)
    report = models.ForeignKey(
        Report,
        related_name="responses",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Report {self.report.id} - {self.message}"
