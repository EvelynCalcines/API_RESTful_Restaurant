# Django and DRF imports
from rest_framework.routers import SimpleRouter

# waning_moon_design import
from .views import WorkshopViewSet, WorkerViewSet, CarViewSet, RepairViewSet

router = SimpleRouter()

router.register(r'workshop', WorkshopViewSet, basename="workshops")
router.register(r'worker', WorkerViewSet, basename="workers")
router.register(r'car', CarViewSet, basename="cars")
router.register(r'repair', RepairViewSet, basename="repairs")

urlpatterns = router.urls
