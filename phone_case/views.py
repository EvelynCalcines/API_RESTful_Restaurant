# Django and DRF imports
from rest_framework.viewsets import ModelViewSet

# waning_moon_design imports
from .serializers import UpdatePhoneCaseSerializer, PhoneCaseSerializer
from phone_case.models import PhoneCase


class PhoneCaseViewSet(ModelViewSet):
    queryset = PhoneCase.objects.all()
    serializer_class = PhoneCaseSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdatePhoneCaseSerializer
        return self.serializer_class
