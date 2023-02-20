from django.http import Http404
from django.http import HttpResponse
from .models import Users
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.views.decorators.csrf import csrf_exempt
import traceback
from .serializer import UserSerializer


def index(request):
    return HttpResponse('Hello everyone. You are in user index')

@api_view(['GET'])
def details(request, user_id):
    res_status = None
    try:
        response = None
        if (user_id == 0):
            user = Users.objects.all()
            serializer = UserSerializer(user, many=True)
        else:
            user = Users.objects.get(id=user_id)
            serializer = UserSerializer(user)
        response = {
            "message": "successful"
        }
        response.update(serializer.data)
        res_status = status.HTTP_200_OK
    except Users.DoesNotExist:
        response = {
            'message':"User does not exits"
        }
        res_status = status.HTTP_406_NOT_ACCEPTABLE
    except Exception as e:
        response = {
            'error': str(e)
        }
        res_status = status.HTTP_400_BAD_REQUEST
    finally:
        return Response(response, status=res_status)


@api_view(['POST'])
@csrf_exempt
def register_user(request):
    response = None
    res_status = None
    try:
        # if (request.method == 'POST'):
            # serializers.E
        # res_dict = json.loads(request.body)
        request_data = request.data['data']
        try:
            user = Users.objects.get(username = request_data['username'])
            response = {
                "response_code":11,
                "message": "User already exist"
            }
            res_status = status.HTTP_200_OK
        except Users.DoesNotExist:
            if len(request_data) == 3:
                user = Users(
                    username = request_data['username'],
                    password = request_data['password'],
                    email = request_data['email']
                )
                user.save()
            response = {
                "response_code":21,
                "message":"User info inserted"
            }
            res_status = status.HTTP_200_OK
        except Exception as e:
            raise e
    except Exception as e:
        response = {
            "response_code":31,
            "error":str(e)
        }
        res_status = status.HTTP_400_BAD_REQUEST
    finally:
        return Response(response, status=res_status)

@api_view(['POST'])
def login_user(request):
    response = {}
    res_status = None
    try:
        # if (request.method == 'GET'):
        user = Users
        # request_body = json.loads(request.data)
        request_body = request.data['data']
        result = user.objects.get(username = request_body['username'])

        if(result.password == request_body['password']):
            response = {
                "response_code":11,
                'status': 'matched',
                'message': 'password matched',
                'id':result.id,
                'username':result.username,
                'email':result.email
                }
        else:
            response = {
                "response_code":21,
                'status': 'not matched',
                'message': 'password did not match'
                }

        res_status = status.HTTP_200_OK
    
    except Users.DoesNotExist:
        response = {
            "response_code": 12,
            "message":"User Dose not exists",
            'status':"no user"
        }
        res_status = status.HTTP_204_NO_CONTENT

    except Exception as e:
        response = {
            "response_code": 31,
            'error': str(e)
        }
        res_status = status.HTTP_400_BAD_REQUEST
    finally:
        return Response(response, status=res_status)

@api_view(['DELETE'])
def delete_user(request):
    response = {}
    res_status = None
    try:
        if (request.data):
            # request_body = json.loads(request.body)
            request_data = request.data['data']
            result = Users.objects.filter(username = request_data['username'])
            for _ in range(len(result)):
                result.delete()
            
        response = {
            "message":"remove successfull"
        }
        res_status = status.HTTP_200_OK
    except Users.DoesNotExist:
        response = {
            "message":"user doesn't exist"
        }
        res_status = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        print(traceback.format_exc())
        response = {
            "error": str(e),
        }
        res_status = status.HTTP_400_BAD_REQUEST
    finally:
        return Response(response, status=res_status)
