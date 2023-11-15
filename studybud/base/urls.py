from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('room/<str:pk>/', views.room, name='room'),
    path('crate-room/', views.create_room, name='create-room'),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
    path('delete-room/<str:pk>/', views.delete_room, name='delete-room'),
    path('delete-message/<str:pk>/', views.delete_message, name='delete-message'),
    path('profile/<str:pk>/', views.user_profile, name='user-profile'),
    path('update-user/', views.update_user, name='update-user'),
    path('topics/', views.topics_page, name='topics'),
    path('activities/', views.activity_page, name='activity'),

]
