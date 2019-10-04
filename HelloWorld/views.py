from annoying.decorators import ajax_request

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from HelloWorld.models import Post, InstaUser, Like, UserConnection
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from HelloWorld.forms import CustomUserCreationForm


# Create your views here.
class HelloDjango(TemplateView):
    template_name = 'hello_world.html'


class PostsView(ListView):
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        current_user = self.request.user
        following = set()
        for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
            following.add(conn.following)
        return Post.objects.filter(author__in=following)





class PostsDetailView(DetailView):
    model = Post
    template_name = 'index_detail.html'


class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'index_create.html'
    fields = '__all__'
    login_url = 'login'


class PostsUpdateView(UpdateView):
    model = Post
    template_name = 'index_update.html'
    fields = ['title']


class PostsDeleteView(DeleteView):
    model = Post
    template_name = 'index_delete.html'
    success_url = reverse_lazy('posts')


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserProfile(LoginRequiredMixin, DetailView):
    model = InstaUser
    template_name = 'user_profile.html'
    login_url = 'login'


class EditProfile(LoginRequiredMixin, UpdateView):
    model = InstaUser
    template_name = 'edit_profile.html'
    fields = ['profile_pic', 'username']
    login_url = 'login'




@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }
