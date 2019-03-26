from django.conf.urls import url
from index.views import index
app_name = 'index'
urlpatterns = [
    # url(r'^register$', views.register, name='register'),
    # url(r'^register_handle$', views.register_handle, name='register_handle'),
    url(r'^index$', index, name='index'),
]

