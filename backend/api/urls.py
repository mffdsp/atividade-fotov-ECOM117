"""web_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers

from photovoltaic import views as photovoltaic_views

router = routers.DefaultRouter()
router.register(r'pvdata', photovoltaic_views.PVDataViewSet)
router.register(r'pvstring', photovoltaic_views.PVStringViewSet)
router.register(r'powerforecast', photovoltaic_views.PowerForecastViewSet)
router.register(r'yieldday', photovoltaic_views.YieldDayViewSet)
router.register(r'yieldmonth', photovoltaic_views.YieldMonthViewSet)
router.register(r'yieldyear', photovoltaic_views.YieldYearViewSet)
router.register(r'yieldminute', photovoltaic_views.YieldMinuteViewSet)
router.register(r'alerttreshold', photovoltaic_views.AlertTresholdViewSet)
router.register(r'settings', photovoltaic_views.SettingsViewSet)

external = routers.DefaultRouter()
external.register(r'apiactions', photovoltaic_views.ExternalAPIViweSet, basename='apiactions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('externalapi/', include(external.urls)),
    path('api-token-auth/', photovoltaic_views.CustomAuthToken.as_view())
]