from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer
class UserNetPublicView(ModelViewSet):
    queryset = UserNet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GetUserNetPublicSerializer
class UserNetPrivateView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetUserNetSerializer
    def get_queryset(self):
        return UserNet.objects.filter(id = self.request.user.id)