from django.urls import path
from . import views
# from .classvViews import UserLogin

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_user),
    path('login', views.LoginUser.as_view()),
    path('remove', views.delete_user),
    path('<int:user_id>', views.details),
    # path('<int:user_id/result')
]
