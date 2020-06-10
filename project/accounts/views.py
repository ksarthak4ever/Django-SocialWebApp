#Django imports.
from django.contrib.auth import authenticate, login

# DRF imports.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

# App imports.
from accounts.models import User
from accounts.serializers import (
	UserLoginSerializer,
	UserSerializer
)
from accounts.decorators import login_required


class UserLoginView(APIView):
    """
    API to login a registered user.
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        req_data = request.data
        login_serializer = UserLoginSerializer(data=req_data)
        login_serializer.is_valid(raise_exception=True)
        # if no validation error
        # logging in the user
        user = authenticate(
        	email=req_data.get('email'),
        	password=req_data.get('password')
        )
        login(request, user)

        return Response(data=login_serializer.data, status=status.HTTP_200_OK)


class SetPasswordView(APIView):
    """
    Should set the password for the given user.
    """
    @login_required
    def put(self, request):
        req_data = request.data
        email = req_data.get('email', None)
        if not email:
        	return Response(
        		dict(message='Email is required to set password'),
        		status=status.HTTP_422_UNPROCESSABLE_ENTITY
        		)
        password = req_data.get('password', None)
        if not password:
        	return Response(
        		dict(message='No password given'),
        		status=status.HTTP_422_UNPROCESSABLE_ENTITY
        	)
        try:
        	user_obj = User.objects.get(email=email)
        except Exception as e:
        	return Response(
        		dict(message='Invalid email id, no user found'),
        		status=status.HTTP_400_BAD_REQUEST
        	)
        user_obj.set_password(password)
        user_obj.save()

        return Response(dict(message='success'), status=status.HTTP_200_OK)


class UsersListView(APIView):
	"""
	API to list all user details in tabular format.
	"""
	@login_required
	def get(self, request):
		users_qs = User.objects.all()
		final_data = list()
		for user_obj in users_qs:
			user_serializer = UserSerializer(user_obj)
			data = user_serializer.data
			# appending link to hyperlink id with in table.
			data['link'] = user_obj.get_absolute_url()
			final_data.append(data) 
		return Response(data=final_data, status=status.HTTP_200_OK)


class UserDetailsView(APIView):
	"""
	API to get a user's details.
	"""
	@login_required
	def get(self, request, user_id=None):
		print(request.user.is_authenticated)
		try:
			user_obj = User.objects.get(id=user_id)
		except Exception as e:
			return Response(
				dict(message='Invalid user id'),
				status=status.HTTP_400_BAD_REQUEST
			)
		user_serializer = UserSerializer(user_obj)

		return Response(data=user_serializer.data, status=status.HTTP_200_OK)


class UserSearchView(APIView):
	"""
	API to search a user based on their phone number.
	"""
	@login_required
	def get(self, request):
		req_data = request.GET 
		phone_number = req_data.get('phone_number', None)

		user_qs = User.objects.filter(phone_number__iexact=phone_number)
		if user_qs.exists():
			user_obj = user_qs.first()
			user_serializer = UserSerializer(user_obj)
			return Response(data=user_serializer.data, status=status.HTTP_200_OK) 

		return Response(data=[], status=status.HTTP_200_OK)