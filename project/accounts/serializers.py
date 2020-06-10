# Django imports.
from django.contrib.auth import authenticate

# DRF imports.
from rest_framework.serializers import (
    # Serializers.
    Serializer, ModelSerializer,

    # Fields.
    CharField, IntegerField,

    # Errors.
    ValidationError,
)

# App imports.
from accounts.models import User


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'name', 'phone_number', 'email')


class UserLoginSerializer(Serializer):
    id_ = IntegerField(read_only=True)
    name = CharField(read_only=True)
    phone_number = CharField(max_length=15, required=False)
    email = CharField(max_length=255, required=True)
    password = CharField(max_length=128, write_only=True)

    def validate(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided a email address
        # and password and that this combination matches one of the users in
        # the database.
        email = data.get('email', None)
        password = data.get('password', None)

        # Raise an exception if email is not provided.
        if not email:
            raise ValidationError("Email is required to log in")

        # Raise an exception if the password is not provided.
        if not password:
            raise ValidationError("Password is required to log in")

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this phone_number/password combination. Notice how
        # we pass `phone_number` as the `username` value since in our User
        # model we set `USERNAME_FIELD` as `phone_number`.
        user = authenticate(username=email, password=password)

        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if not user:
            raise ValidationError(
                'user with this email and password was not found'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.

        return dict(
            id_=user.id, name=user.name,
            phone_number=user.phone_number, email=user.email, 
        )