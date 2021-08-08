from core.api.views import TaskResultsViewSet, TaskerAPIView
from django.urls import include,path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"task-results", TaskResultsViewSet)


urlpatterns = [
            path("", include(router.urls)),
            # path('sendsms/',SendSMSapiView.as_view(),name= "twilio-sms"),
            path('tasker/',TaskerAPIView.as_view(), name= "Tasker"),
]