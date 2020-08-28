"""bugtracker_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from bugs_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ticket/<int:ticket_id>/edit/', views.ticket_edit_view),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket'),
    path('user/<int:user_id>/', views.user_details),
    path('new_ticket/', views.ticket_submit_view, name='new_ticket'),
    path('in_progress/', views.ticket_in_progress, name='in_progress'),
    path('completed/', views.ticket_completed, name='completed'),
    path('invalid/', views.ticket_invalid, name='invalid'),
    path('submit/', views.ticket_submit_view, name='submit_ticket'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]
