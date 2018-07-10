from rest_framework.routers import SimpleRouter

from apiscrap.views import RobotModelViewSet

router = SimpleRouter()

router.register('robot', RobotModelViewSet)

urlpatterns = router.urls
