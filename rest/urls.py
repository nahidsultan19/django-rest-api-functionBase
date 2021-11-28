from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiView),
    path('list/', views.List, name='list'),
    path('detail/<str:pk>/', views.Detail, name='detail'),
    path('create/', views.Create, name='create'),
    path('update/<str:pk>/', views.Update, name='update'),
    path('delete/<str:pk>/', views.Delete, name='delete')
]
