# Django and DRF imports
from rest_framework.routers import SimpleRouter

# waning_moon_design import
from .views import RestaurantViewSet

router = SimpleRouter()

router.register(r'restaurant', RestaurantViewSet, basename="restaurants")

urlpatterns = router.urls
