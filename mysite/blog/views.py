# from re import L
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required

from blog.forms import AddPostForm, LoginUserForm, RegisterUserForm
from blog.forms import ContactForm

from .models import *
from .utils import *


class BlogIndex(DataMixin, ListView):

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title='Home')

        return context | c_def

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related("cat")


class Categories(DataMixin, ListView):

    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title=str(context['posts'][0].cat))
        return context | c_def

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related("cat")


class Post(DetailView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('home')

    # login_url = reverse_lazy('home')
    redirect_field_name = 'home'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title='Add post')
        return context | c_def

# @login_required


def about(request):
    context = {
        "title": "about",
    }
    return render(request, 'blog/about.html', context=context)


# def show_post(request, post_slug):
    # post = get_object_or_404(Blog, slug=post_slug)
    # context = {
    # "title": post.title,
    # "post": post,
    # "cat_selected": post.cat_id,
    # }
    # return render(request, 'blog/post.html', context=context)


def contacts(request):
    context = {
        "title": "contacts",
    }
    return render(request, 'blog/about.html', context=context)


# def add_post(request):
    # if request.method == "POST":
    # form = AddPostForm(request.POST, request.FILES)
    # if form.is_valid():
    # form.save()
    # return redirect('home')
    # else:
    # form = AddPostForm()
    # context = {
    # "title": "add post",
    # "form": form,
    # }
    # return render(request, 'blog/add_post.html', context=context)


# def category(request, cat_slug):
    # posts = Blog.objects.filter(cat_id=Category.objects.get(slug=cat_slug).pk)

    # if len(posts) == 0:
    # raise Http404()
    # context = {
    # "title": "category",
    # "posts": posts,
    # }
    # return render(request, 'blog/index.html', context=context)
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title='Contacts')
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title='Register')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title='Login')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


# Create your views here.
