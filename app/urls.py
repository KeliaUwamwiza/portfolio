# from django.urls import path
# from . import views

# urlpatterns = [
    
#     # path('', views.project_list, name='project_list'),  # Read (List)
#     # path('project/<int:pk>/', views.project_detail, name='project_detail'),  # Read (Detail)
#     # path('project/add/', views.project_create, name='project_create'),  # Create
#     # path('project/<int:pk>/edit/', views.project_update, name='project_update'),  # Update
#     # path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),  # Delete
#     # path('user/register/', views.register, name='register'),
#     # path('user/login/', views.user_login, name='login'),
#     # path('user/logout/', views.user_logout, name='logout'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    path('update/', views.update_portfolio, name='update_portfolio'),
    path('delete/', views.delete_portfolio, name='delete_portfolio'),
]
