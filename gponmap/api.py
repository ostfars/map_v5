from rest_framework import routers
from gponmap.viewsets import PointViewSet, QgisPointViewSet

router = routers.DefaultRouter()
router.register(r"gponmap", PointViewSet)
router.register(r"gponmap", QgisPointViewSet)


urlpatterns = router.urls
