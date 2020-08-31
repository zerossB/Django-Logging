import logging

from django.shortcuts import render
from rest_framework import response, views, permissions, status

# logger = logging.getLogger("django")
logger = logging.getLogger(__name__)

# Create your views here.
class HomeView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        print(__name__)
        logger.info("TESTE")
        logger.debug("TESTADO")
        return response.Response(status=status.HTTP_200_OK)
