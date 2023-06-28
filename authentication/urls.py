# Django and DRF imports
from rest_framework.routers import SimpleRouter
from django.urls import path

# waning_moon_design import
from .views import RegisterViewSet, UserViewSet, UserLoginView, CommentViewSet


router = SimpleRouter()


router.register(r'register', RegisterViewSet, basename="register")
router.register(r'users', UserViewSet, basename="users")
router.register(r'comments', CommentViewSet, basename="comments")


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='master_data'),
]

urlpatterns = urlpatterns + router.urls
