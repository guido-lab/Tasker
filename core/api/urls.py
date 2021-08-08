from core.api.views import TaskerAPIView
from django.urls import include,path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
            path("", include(router.urls)),
            # path('sendsms/',SendSMSapiView.as_view(),name= "twilio-sms"),
            path('tasker/',TaskerAPIView.as_view(), name= "Tasker"),
]