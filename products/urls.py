from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='ProductViewSet')
urlpatterns = router.urls
