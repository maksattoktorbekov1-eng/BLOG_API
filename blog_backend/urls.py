from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_blog/v1/', include('api_blog.urls')),
    path('api_blog/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api_blog/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api_blog/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api_blog/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]