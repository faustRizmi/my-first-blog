from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^signin/$',views.signin),
    url(r'^signup/$',views.signup,name='signup'),
	url(r'^',views.home),

]
