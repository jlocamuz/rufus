from django.urls import include, path
from .views import MenuViewSet, DishViewSet, DishItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menus', MenuViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'dishitems', DishItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = router.urls