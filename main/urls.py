from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from . import views



router = DefaultRouter()

router.register(r'products', views.ProductView)
router.register(r'categories', views.CategoryView)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
