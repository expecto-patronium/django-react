from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .renderer import UserRenderer
from .models import TodoModel
from .serializers import TodoSerializer, RegisterSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime
from django.shortcuts import render


# from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_todo(request, pk):
    data = TodoModel.objects.get(id=pk)
    serializer = TodoSerializer(data)
    return Response(serializer.data)


def index(request, *args, **kwargs):
    return render(request, 'index.html')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_todo(requests):
    print("-----------", requests.data)
    requests.data["updated_at"] = datetime.now()
    serializer = TodoSerializer(data=requests.data, many=False)
    if serializer.is_valid():
        serializer.save(user=requests.user)
        return Response(serializer.data)
    return Response({"status": "serializer is not valid"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_todo(requests, pk):
    print(requests.data)
    task = TodoModel.objects.get(id=pk)
    serializer = TodoSerializer(instance=task, data=requests.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"status": "serializer is not valid"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_todo(requests, pk):
    task = TodoModel.objects.get(id=pk)
    task.delete()
    return Response({"status": "Todo deleted successfully"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def all_todo(request):
    task = TodoModel.objects.filter(user=request.user)
    serialize = TodoSerializer(task, many=True)
    return Response(serialize.data)


class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


@api_view(["POST"])
def register_user(requests):
    serializer = RegisterSerializer(data=requests.data)
    if serializer.is_valid():
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserprofileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, requests):
        serializer = UserProfileSerializer(requests.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(["POST"])
# def add_comment(requests):
#     serializer = CommentSerializer(data=requests.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
#
#
# @api_view(["GET"])
# def get_comments(requests, pk):
#     todo = TodoModel.objects.get(id=pk)
#     comments = todo.comments.all()
#     serializer = CommentSerializer(comments, many=True)
#     return Response(serializer.data)

# class TodoList(APIView):
#     def get(self, request, pk):
#         todo = self.get_object(pk)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         todo = self.get_object(pk)
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, requests, pk):
#         todo = self.get_object(pk)
#         todo.delete()
#         return Response(status=status.HTTP_400_BAD_REQUEST)
