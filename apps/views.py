from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .serializers import AppSerializer
from rest_framework.decorators import action

from .models import App


class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    queryset = App.objects.all()

    @action(methods=['put'], detail=True, url_path="update")
    def update_api_key(self, request, pk=None):
        app = get_object_or_404(self.queryset, api_key=pk)
        old_key = app.api_key
        app.update_key()
        new_key = app.api_key
        return Response({
            "message": "your api key is updated",
            "old_api_key": old_key,
            "new_api_key": new_key
        })

    
    @action(methods=['get'], detail=True, url_path="info")
    def get_info(self, request, pk=None):
        app = get_object_or_404(self.queryset, api_key=pk)
        serializer = AppSerializer(app)
        return Response({"app": serializer.data})