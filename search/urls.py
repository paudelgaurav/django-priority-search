from rest_framework.routers import DefaultRouter

from .views import ProductReadOnlyViewSet

router = DefaultRouter()

router.register(r"products", ProductReadOnlyViewSet, basename="products")

urlpatterns = router.urls
