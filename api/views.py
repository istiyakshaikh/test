from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailSerializer, UserCreateSerializer
from .models import User_details
from django.db.models import Q
import secrets



def get_token():
    token = secrets.token_hex(32)
    return token


def user_token():
    token = secrets.token_hex(5)
    user = 'user-'+token
    return user


class UserList(APIView):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            if request.headers.get('Token') is not None:
                queryset = User_details.objects.filter(
                    token=request.headers.get('Token'))
                serializer = UserDetailSerializer(queryset, many=True)
                if serializer.data == [] or serializer.data[0].get('is_deleted') == True:
                    return Response({"Error": ["User is not register or User is deleted!!"]}, status=status.HTTP_404_NOT_FOUND)
                return Response(serializer.data[0])
            else:
                return Response({"Error": "Bad Request!!!"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer = UserCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['user_name'] = user_token()
                serializer.validated_data['token'] = get_token()
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"Error": "Please Enter correct Data!"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if request.method == "PUT":
            try:
                if request.data.get('token') is not None:
                    item = User_details.objects.get(
                        token=request.data.get('token'))
                    data = UserDetailSerializer(instance=item, data=request.data)
        
                if data.is_valid(raise_exception=True):
                    if User_details.objects.filter(Q(user_email__iexact=request.data.get('user_email')) & Q(is_deleted=False)).exists() and request.data.get('user_email') is not None:
                        queryset = User_details.objects.filter(
                            Q(user_email__iexact=request.data.get('user_email')) & Q(is_deleted=False))
                        serializer = UserCreateSerializer(queryset, many=True)
                        return Response(serializer.data[0], status=status.HTTP_200_OK)
                    if User_details.objects.filter(Q(google_id__iexact=request.data.get('google_id')) & Q(is_deleted=False)).exists() and request.data.get('google_id') is not None:
                        queryset = User_details.objects.filter(
                            Q(google_id__iexact=request.data.get('google_id')) & Q(is_deleted=False))
                        serializer = UserCreateSerializer(queryset, many=True)
                        return Response(serializer.data[0], status=status.HTTP_200_OK)
                    if User_details.objects.filter(Q(facebook_id__iexact=request.data.get('facebook_id')) & Q(is_deleted=False)).exists() and request.data.get('facebook_id') is not None:
                        queryset = User_details.objects.filter(
                            Q(facebook_id__iexact=request.data.get('facebook_id')) & Q(is_deleted=False))
                        serializer = UserCreateSerializer(queryset, many=True)
                        return Response(serializer.data[0], status=status.HTTP_200_OK)
                    if User_details.objects.filter(Q(apple_id__iexact=request.data.get('apple_id')) & Q(is_deleted=False)).exists() and request.data.get('apple_id') is not None:
                        queryset = User_details.objects.filter(
                            Q(apple_id__iexact=request.data.get('apple_id')) & Q(is_deleted=False))
                        serializer = UserCreateSerializer(queryset, many=True)
                        return Response(serializer.data[0], status=status.HTTP_200_OK)
                    data.validated_data['is_guest'] = False
                    data.save()
                    return Response(data.data, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            except :
                return Response({"Error": "Please Enter correct Data!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                if request.headers.get('Token') is not None:
                    queryset = User_details.objects.filter(
                        token=request.headers.get('Token'))
                    if queryset.exists():
                        queryset.update(is_deleted=True)
                        return Response({"Deleted"}, status=status.HTTP_202_ACCEPTED)
                    else:
                        return Response({"Error": ["User is not register or User is deleted!!"]}, status=status.HTTP_404_NOT_FOUND)
            except:
                return Response({"Error": "Id not found!"}, status=status.HTTP_404_NOT_FOUND)



