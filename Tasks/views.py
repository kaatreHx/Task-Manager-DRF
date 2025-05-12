from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_201_CREATED
from .pagination import TaskPagination

class Registration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=HTTP_201_CREATED)
        return Response(serializer.errors)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TaskPagination

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
