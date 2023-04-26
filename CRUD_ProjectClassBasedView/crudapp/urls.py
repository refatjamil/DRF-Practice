from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.UserAddShow.as_view(),name='addandshow'),
    path('delete/<int:id>/',views.UserDelete.as_view(),name='delete'),
    path('update/<int:id>/',views.UserUpdate.as_view(),name='update'),
]