from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Users
from rest_framework import status
from users.serializer import UserSerializer

class UserLogin(View):
    user_serializer = UserSerializer()
    # user = Users
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
       print('requrest = ', request)
       return Response({'message':'api called'})