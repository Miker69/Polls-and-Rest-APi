from django.urls import path
from django.conf.urls import url
from .views import PollView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Pols API",
      default_version='v1',
      description="Api description",
         ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('active/polls/', PollView.as_view(), name='get_active_polls'),
    path('completed/polls/<int:uid>/', PollView.as_view(), name='get_completed_polls'),
    path('take/poll/', PollView.as_view(), name='post_poll'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
