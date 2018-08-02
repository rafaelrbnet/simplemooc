from django.urls import path, include
from django.contrib import auth
from django.contrib.auth import views as auth_views
from simplemooc.accounts import views as accounts_views
from . import views

app_name = 'accounts'

urlpatterns = [
	path('', accounts_views.dashboard, name='dashboard'),
	path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout/', accounts_views.logout, name='logout'),
	path('cadastre-se/', accounts_views.register, name='register'),
	path('nova-senha/', accounts_views.password_reset, name='password_reset'),
	path('confirmar-nova-senha/<key>', accounts_views.password_reset_confirm, name='password_reset_confirm'),
	path('editar/', accounts_views.edit, name='edit'),
	path('editar-senha/', accounts_views.edit_password, name='edit_password')
]