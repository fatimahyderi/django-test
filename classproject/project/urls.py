from django.urls import path
from . import views
app_name='project'


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('portfolio/',views.portfolio,name='portfolio'),

]
