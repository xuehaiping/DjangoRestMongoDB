from django.conf.urls import include, url
from guide import views

from rest_framework.routers import DefaultRouter

app_name = 'guide'

router = DefaultRouter()
router.register('guide-viewset', views.GuideViewSet, base_name='guide-viewset')

urlpatterns = [
    url(r'', include(router.urls)),
]
