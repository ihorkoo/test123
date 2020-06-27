from django.urls import path
from . import views


urlpatterns = [
    path('', views.form_for_curr, name='dowload_curr'),
    path('<str:date>', views.dowload_curr_file, name='dowload_curr_file')

]
