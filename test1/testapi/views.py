from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ViewSet
from .models import UserModel
from .serializers import RegisterSerializer
from rest_framework.response import Response


class RegisterViewSet(ViewSet):
    # create user
    def create(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, 422)
            serializer.save()
            return Response(serializer.data, 201)
        except Exception as e:
            return Response({'message': str(e)}, 500)
    
    # get particular user
    def retrieve(self, request, pk=None):
        try:
            queryset = UserModel.objects.get(pk=pk)
            serializer_class = RegisterSerializer(queryset)
            return Response(serializer_class.data, 200)
        except Exception as e:
            return Response("error " + str(e), 500)

    # get list of users based on query parameters
    def list(self, request):
        try:
            if 'sort' in request.GET:
                queryset = UserModel.objects.all().order_by(request.GET['sort'])
            else:
                queryset = UserModel.objects.all()
            serializer_class = RegisterSerializer(queryset, many=True)
            result = []
            if 'name' in request.GET:
                for i in serializer_class.data:
                    if (request.GET['name'] in i['first_name']) or (request.GET['name'] in i['last_name']):
                        result.append(i)
            else:
                result=serializer_class.data
            # Considering either limit and page both are in the request or both are not in the request
            if 'limit' in request.GET:
                limit, page= int(request.GET['limit']),int(request.GET['page'])
                return Response(result[(page-1)*limit:page*limit],200)
            else:
                return Response(result,200)
        except Exception as e:
            return Response(str(e), 500)
    
    # updating a user details
    def put(self, request, pk=None):
        try:
            user_detail = UserModel.objects.filter(pk=pk).first()
            serializer = RegisterSerializer(user_detail, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, 422)
            serializer.save()
            if 'password' in request.data:
                user_detail.password = make_password(request.data['password'], hasher='default')
                user_detail.save()
            return Response(serializer.data)
        except Exception as e:
            return Response('some exception occurred' + str(e), 500)

    # deleting a user
    def destroy(self, request, pk=None):
        try:
            user_detail = UserModel.objects.get(pk=pk)
            user_detail.delete()
        except Exception as e:
            return Response('some exception occurred ' + str(e), 500)
        return Response({"message":'record Deleted successfully'}, 200)
