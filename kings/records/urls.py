from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('views/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('views/add/addrecord/', views.addrecord, name='addrecord'),
    path('views/update/<int:id>', views.update, name='update'),
    path('views/update/updaterecord/<int:id>',
         views.updaterecord, name='updaterecord'),
    path('views/delete/<int:id>', views.delete, name='delete'),
    path('jsondata/', views.jsondata, name="jsondata"),
]
