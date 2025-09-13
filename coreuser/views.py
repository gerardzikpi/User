from django.shortcuts import redirect
from rest_framework import viewsets,authentication,permissions,generics,status
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm
from .models import CoreUser
from .forms import RegistrationForm
from .serializers import CoreUserSerializer

# Create your views here
class CoreUserViewset(viewsets.ModelViewSet):
    serializer_class = CoreUserSerializer
    queryset = CoreUser.objects.all()
    authentiction_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        usernames = [user.name for user in CoreUser.objects.all()]
        return Response(Username)

# def login(request):
#     LoginForm = AuthenticationForm
#     if LoginForm.is_valid:
#         return redirect "homepage"
#     else:
#         LoginForm = AuthenticationForm
#     return Response(login)
    

