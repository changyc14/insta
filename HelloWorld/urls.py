"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from HelloWorld.views import HelloDjango, PostsView, PostsDetailView, \
PostsCreateView, PostsUpdateView, PostsDeleteView, addLike, UserProfile, EditProfile

urlpatterns = [
    path('helloworld', HelloDjango.as_view(), name='home'),
    path('', PostsView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostsDetailView.as_view(), name='posts_detail'),
    path('posts/new/', PostsCreateView.as_view(), name='make_post'),
    path('posts/update/<int:pk>/', PostsUpdateView.as_view(), name='posts_update'),
    path('posts/delete/<int:pk>/', PostsDeleteView.as_view(), name='posts_delete'),
    path('posts/like', addLike, name='addLike'),
    path('user_profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    ]
