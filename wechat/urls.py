from django.conf.urls import url
from wechat import views



urlpatterns = [
    url(r'^$', views.index),
    url(r'^auth/', views.auth),

]
