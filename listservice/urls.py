from django.conf.urls import include
from django.conf.urls import url
from listservice import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
		url(r'^list/(?P<user>[\s\S]+)/owner/(?P<repo>[\s\S]+)/repo/$', views.get_issues_list, name="list-issues"),
]