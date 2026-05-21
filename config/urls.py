from django.contrib import admin
from django.urls import path
from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.job_list, name='job_list'),
    path('add/', views.job_add, name='job_add'),
    path('edit/<int:pk>/', views.job_edit, name='job_edit'),
    path('delete/<int:pk>/', views.job_delete, name='job_delete'),
]