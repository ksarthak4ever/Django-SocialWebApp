# Django imports.
from django.urls import path, include
from django.views.generic.base import TemplateView

# App imports.
from accounts.views import (
	UserLoginView, SetPasswordView,
	UserDetailsView, UsersListView,
	UserSearchView
)


urlpatterns = [
    # # Route to register users.
    # path(r'register/', UserRegisterView.as_view(), name='user-register'),
    # Route to login registered users.
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    path('login/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),

    # APIs
    path('normal_login/', UserLoginView.as_view(), name='user-login'),
    path('set_password/', SetPasswordView.as_view(), name='set-password'),
    path('user/all/', UsersListView.as_view(), name='users-list'),
    path(r'user/<int:user_id>/', UserDetailsView.as_view(), name='user-details'),
    path('user/search/', UserSearchView.as_view(), name='user-search')
]