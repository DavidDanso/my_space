from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.adminPage, name='home'),
    path('user/', views.user_feed, name='user'),
    path('project_update/<str:pk>/', views.project_update, name='project_update'),
    path('meeting_update/<str:pk>/', views.meeting_update, name='meeting_update'),
    path('deal_update/<str:pk>/', views.deal_update, name='deal_update'),
    path('deleteCurrentProject/<str:pk>/', views.deleteCurrentProject, name='deleteCurrentProject'),
    path('deleteCurrentMeeting/<str:pk>/', views.deleteCurrentMeeting, name='deleteCurrentMeeting'),
    path('deleteCurrentDeal/<str:pk>/', views.deleteCurrentDeal, name='deleteCurrentDeal'),
    path('edit_profile/', views.accountSettingsUpdate, name='edit_profile'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),

    path('user_profile/<str:pk>/', views.userProfile, name='user_profile'),
    path('deleteUserProfile/<str:pk>/', views.deleteUserProfile, name='deleteUserProfile'),

    
]