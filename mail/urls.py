from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    # path('<int:resident_id>/', views.resident, name='resident')
    path('residents', views.residents, name='residents'),
    path('history/<int:resident_id>', views.history, name='history')
]