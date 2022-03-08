"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from account import login_render

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^index$', login_render.web_index, name='web_index'),
    url(r'^login$', login_render.web_login, name='web_login'),
    url(r'^logout$', login_render.web_logout, name='web_logout'),
]

urlpatterns += [
    url(r'^bs/', include('competition.urls', namespace='bs')),  # 比赛
    url(r'^api/', include('api.urls', namespace='api')),  # 接口
    url(r'^biz/', include('business.urls', namespace='biz')),  # 机构
    url(r'^ana/', include('analysis.urls', namespace='ana')),  # 分析
]

urlpatterns += [
    url(r'^auth/', include('account.urls', namespace='auth')),  # 微信授权
]

handler403 = login_render.error
handler404 = login_render.error
handler500 = login_render.error

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "[Quizz 管理系统]"
