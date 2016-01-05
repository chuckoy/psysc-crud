# django
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

# views
from .views import IndexView

# django admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^demo/$', IndexView.as_view(), name='index'),
]
