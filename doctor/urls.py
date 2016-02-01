from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register_view, name = 'register'),
    url(r'^login', views.login_view, name = 'login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^postTemp/$', views.postTemp_view, name='postTemp'),
    url(r'^newPatient/$', views.new_patient_view, name =  'newPatient'),
    url(r'^analysis/$', views.analysis_view, name ='analysis'),
    url(r'^getTempData/$', views.get_data_view, name = 'getData'),
]