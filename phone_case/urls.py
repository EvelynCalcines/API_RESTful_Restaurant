# Django and DRF imports
from rest_framework.routers import SimpleRouter

# waning_moon_design import
from .views import PhoneCaseViewSet, MePhoneCaseView

router = SimpleRouter()

router.register(r'PhoneCase', PhoneCaseViewSet, basename="PhoneCases")
router.register(r'me/PhoneCases', MePhoneCaseView, basename="me_PhoneCases")

urlpatterns = router.urls
