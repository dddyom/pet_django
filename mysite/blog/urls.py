from django.urls import path
from blog.views import *
# from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', cache_page(60)(BlogIndex.as_view()), name='home'),
    path('', BlogIndex.as_view(), name='home'),
    path('about', about, name='about'),
    path('post/<slug:post_slug>/', Post.as_view() , name='post'),
    path('contacts', ContactFormView.as_view(), name='contacts'),
    path('add_post', AddPost.as_view(), name='add_post'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('category/<slug:cat_slug>', Categories.as_view(), name='category'),
]
