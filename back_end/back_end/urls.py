"""back_end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls #DOCUMENTACIÓN DE LAS URL
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

from user.viewsets import CustomerViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='Customers')



urlpatterns = [
    path('admin/', admin.site.urls),
    #URL DE AUTENTICACIÓN
    path('api/docs/', include_docs_urls(title='Nuestra API')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('api/', include(router.urls)),
]
