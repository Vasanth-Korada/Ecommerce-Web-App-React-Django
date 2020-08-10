import re
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import uuid


@csrf_exempt
def signin(request):

    if not request.method == 'POST':
        return JsonResponse({"error": "Send a post request with valid params"})

    username = request.POST['email']
    password = request.POST['password']
    # validation part
    if not re.match("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", username):
        return JsonResponse({
            "error": "Enter a valid email"
        })
    if len(password) < 3:
        return JsonResponse({
            "error": "Password needs to be atleast 3 characters"
        })

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):

            user_dict = UserModel.objects.filter(
                email=username).values().first()
            user_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({
                    "error": "Previous session exists!"
                })

            token = uuid.uuid4()  # generating session token

            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({
                "token": token,
                "user": user_dict
            })
        else:
            return JsonResponse({
                "error": "Incorrect Password"
            })
    except:
        if UserModel.DoesNotExist:
            return JsonResponse({
                "error": "User Not Found."
            })


def signout(request, id):

    logout(request)
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        try:
            user.session_token = "0"
            user.save()
        except:
            return JsonResponse({
                "error": "Signout error"
            })

    except UserModel.DoesNotExist:
        return JsonResponse({
            "error": "Invalid User ID"
        })

    return JsonResponse({"success": "Logout success"})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            # return [permission() for permission in self.permission_classes_by_action[self.action]]
            return []
        except KeyError:
            return [permission() for permission in self.permisssion_classes]
