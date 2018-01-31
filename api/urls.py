from rest_framework import routers

from .views.npo import NPOViewSet
from .views.user import UserViewSet


router = routers.SimpleRouter()

router.register(r'npos', NPOViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
