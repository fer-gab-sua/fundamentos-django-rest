from rest_framework.routers import DefaultRouter
from my_site.api.views import ProductoViewSet , ArticleViewSet


router = DefaultRouter()
router.register('user',ProductoViewSet, basename='productos')
router.register('article',ArticleViewSet, basename='article')
urlpatterns = router.urls