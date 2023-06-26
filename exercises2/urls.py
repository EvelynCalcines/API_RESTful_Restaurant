# Django and DRF imports
from rest_framework.routers import SimpleRouter

# waning_moon_design import
from .views import BuildingViewSet, FloorViewSet, MeFloorView

router = SimpleRouter()

router.register(r'buildings', BuildingViewSet, basename="buildings")
router.register(r'floors', FloorViewSet, basename="floors")
router.register(r'me/floors', MeFloorView, basename="me_floors")

urlpatterns = router.urls
