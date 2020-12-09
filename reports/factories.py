import factory
from django.conf import settings

from .models import Report, ReportResponse


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")


class ReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Report

    message = factory.Faker("sentence", nb_words=10)
    author = factory.SubFactory(UserFactory)

    @factory.post_generation
    def supervisors(self, create, extracted):
        if not create:
            return

        if extracted:
            for supervisor in extracted:
                self.supervisors.add(supervisor)


class ReportResponseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ReportResponse

    message = factory.Faker("sentence", nb_words=10)
    report = factory.SubFactory(ReportFactory)
    author = factory.SubFactory(UserFactory)
