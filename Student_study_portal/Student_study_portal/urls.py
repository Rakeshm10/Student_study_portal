"""
URL configuration for Student_study_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include  # Add this line to import 'include'

from django.contrib import admin
from Dashboard import views as dash_views
from django.contrib.auth import views as auth_views
# from django.views.generic.base import RedirectView
from django.shortcuts import redirect


# from django.urls import path

# from django.shortcuts import redirect

# def redirect_to_admin(request):
#     if request.user.is_authenticated:
#         if request.user.username == 'root' and request.user.check_password('Rakesh123'):
#             return redirect('/admin/')
#         else:
#             return redirect('/')
#     else:
#         return redirect('/')  # Redirect unauthenticated users to the login page



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Dashboard.urls')),
    path('register/',dash_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="Dashboard/login.html"), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="Dashboard/logout.html"), name='logout'),
    # path('accounts/login/', LoginView.as_view(), name='login'),  # Default Django login view
    # path('', RedirectView.as_view(url='/admin/' if name == 'root' and password == 'Rakesh123' else '/')),  # Redirect based on condition
    # Add other app URLs here
    # path('', redirect_to_admin),
    


]

from django.conf import settings
from django.conf.urls.static import static

# Only use this for development purposes.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
