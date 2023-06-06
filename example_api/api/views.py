from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status



class HelloView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        status_code = status.HTTP_200_OK
        response = {'message':'hello!'}
        return Response(response, status=status_code)