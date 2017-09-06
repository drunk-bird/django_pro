from django.conf.urls import url
from wechat import views



urlpatterns = [
    url(r'^index/', views.index),
    url(r'^auth/', views.index),

]
