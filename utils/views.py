# Django and DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

# waning_moon_design import
from phone_case.models import ColorType


class MasterDataAPIView(APIView):
    def get(self, request):
        color_choices = ColorType.get_all_choices()

        return Response(
            {
                'color_choices': color_choices,
            },

        )
