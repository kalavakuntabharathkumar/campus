from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import health, StudentViewSet, RecruiterViewSet, OpportunityViewSet, ApplicationViewSet
router=DefaultRouter()
router.register('students',StudentViewSet)
router.register('recruiters',RecruiterViewSet)
router.register('opportunities',OpportunityViewSet)
router.register('applications',ApplicationViewSet)
urlpatterns=[path('health/',health),path('',include(router.urls))]
