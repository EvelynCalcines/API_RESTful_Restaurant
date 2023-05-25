# Django and DRF imports
from rest_framework.viewsets import ModelViewSet


# waning_moon_design imports
from .serializers import UpdatePhoneCaseSerializer, ListPhoneCaseSerializer, CreatePhoneCaseSerializer
from phone_case.models import PhoneCase


class PhoneCaseViewSet(ModelViewSet):
    queryset = PhoneCase.objects.all()
    serializer_class = ListPhoneCaseSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdatePhoneCaseSerializer
        elif self.action == "create":
            return CreatePhoneCaseSerializer
        return self.serializer_class
