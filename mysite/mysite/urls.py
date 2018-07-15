"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

#from django.conf.urls import url, include
#from django.contrib import admin

#urlpatterns = [
#    url(r'^', include('elections.urls')), #localhost:8000으로 요청이 들어오면 elections.urls로 전달
#    url(r'^admin/', include(admin.site.urls)), #app 접속을 위해 include를 씁니다.
#]

from django.contrib import admin
from django.urls import path, include #include와 urls를 사용하기위해 import 해줘야 하는것
# from django.conf.urls import url,include <-- 이 import 대신 위의 import를 사용합니다.

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('elections.urls')), #elections app을 include 해주는것임. 
]