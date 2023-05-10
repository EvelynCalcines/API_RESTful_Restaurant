# Django and DRF imports
from rest_framework.routers import SimpleRouter

# waning_moon_design import
from .views import PhoneCaseViewSet

router = SimpleRouter()

router.register(r'PhoneCase', PhoneCaseViewSet, basename="PhoneCases")

urlpatterns = router.urls
