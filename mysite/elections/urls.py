#C\Code\mysite\elections\urls.py
#from django.conf.urls import url
#from . import views #.은 현재 폴더(elections)를 의미합니다.

#urlpatterns = [
#    url(r'^$', views.index), #위의 urls.py와는 달리 include가 없습니다.
#]

from django.urls import path, include
from . import views #.은 현재폴더의 디렉토리라는뜻. 즉 현재폴더의 views.py를 import하는것임

urlpatterns = [
	path('', views.index),
	path('areas/<str:area>/',views.areas),
	path('areas/<str:area>/results',views.results),
	path('polls/<int:poll_id>/', views.polls), #이 url에 대한 요청을 views.polls가 처리하게 만듭니다.
]

# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^areas/(?P<area>.+)/$', views.areas)
#     #url(r'^areas/(?P<area>\d+)/$', views.areas) <- 숫자만 거르고 싶을때 
# ]