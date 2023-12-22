from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (BaseView, SignUpView,
                    EmployeeLoginView, EmployeeLogoutView, EmployeeViewSet)

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(),
         name="token"),
    path("api/refresh_token/", TokenRefreshView.as_view(),
         name="refresh_token"),
    path("ckeditor/", include('ckeditor_uploader.urls')),
    path('login/', EmployeeLoginView.as_view(),
         name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', EmployeeLogoutView.as_view(),
         name='logout'),
    path('employees/', include('employees.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
