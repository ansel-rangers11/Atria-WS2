from rest_framework import routers

from .views.npo import NPOViewSet


router = routers.SimpleRouter()

router.register(r'npos', NPOViewSet)

urlpatterns = router.urls
