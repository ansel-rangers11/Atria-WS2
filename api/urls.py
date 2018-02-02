from rest_framework import routers

from .views.npo import NPOViewSet
from .views.user import UserViewSet
from .views.opportunity import OpportunityViewSet


router = routers.SimpleRouter()

router.register(r'npos', NPOViewSet)
router.register(r'users', UserViewSet)
router.register(r'opportunity', OpportunityViewSet)

urlpatterns = router.urls
