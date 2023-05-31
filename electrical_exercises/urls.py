# Django and DRF imports
from rest_framework.routers import SimpleRouter

# waning_moon_design import
from .views import TelevisionViewSet, FridgeViewSet

router = SimpleRouter()

router.register(r'Television', TelevisionViewSet, basename="Television")
router.register(r'Fridge', FridgeViewSet, basename="Fridge")

urlpatterns = router.urls

