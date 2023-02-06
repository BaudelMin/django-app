from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_user),
    path('login', views.login_user),
    path('remove', views.delete_user),
    path('<int:user_id>', views.details),
    # path('<int:user_id/result')
]
