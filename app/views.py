from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Post
from app.producer import publish
from app.serializers import UserSerializer, PostSerializer


# Create your views here.
def home(request):
    return HttpResponse("<h1>This is my start page</h1>")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes((permissions.IsAuthenticated,))
class PostDetail(APIView):

    def get(self, request, id):
        data = Post.objects.get(pk=id)
        serializer = PostSerializer(data, many=False)
        return Response(serializer.data)


@permission_classes((permissions.IsAuthenticated,))
class PostCreate(APIView):
    def post(self, request):
        try:
            serializer = PostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Пост успешно добавлен.'})
        except Exception as ex:
            return Response({'message': 'Ошибка в передаче данных.', 'Ошибка': ex})


@permission_classes((permissions.IsAuthenticated,))
class Test(APIView):
    print("==Test==")

    def get(self, request):
        try:
            publish(request.data['method'], request.data)
        except Exception as ex:
            print("Finally", ex)
        return Response({'message': 'OK.'})
