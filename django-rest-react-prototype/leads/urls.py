from django.urls import path
from . import views

urlpatterns = [
  path('api/lead/', views.LeadListCreate.as_view() ),
  path('current_user/', views.current_user),
  path('users/', views.UserList.as_view()),
  path('steamid/', views.steamID),
  path('processWishlist/', views.processWishlist),
  path('like/', views.like),
]
