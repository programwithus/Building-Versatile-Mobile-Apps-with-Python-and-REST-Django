from django.urls import path
from . import views


urlpatterns = [
    path('', views.PizzeriaListAPIView.as_view(), name='pizzeria_list'),
    path('<int:id>/', views.PizzeriaRetrieveAPIView.as_view(),
         name='pizzeria_detail'),
    path('create/', views.PizzeriaCreateAPIView.as_view(), name='pizzeria_create'),
    path('update/<int:id>/', views.PizzeriaRetrieveUpdateAPIView.as_view(),
         name='pizzeria_update'),
    path('delete/<int:id>/', views.PizzeriaDestroyAPIView.as_view(),
         name='pizzeria_delete'),

]
