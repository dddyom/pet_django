from django import template
from blog.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if filter:
        return Category.objects.filter(pk=filter)
    return Category.objects.all()


@register.inclusion_tag('blog/right_sidebar.html', name='show_cats')
def show_categories(sort=None):
    if sort:
        cats = Category.objects.order_by(sort)
    else:
        cats = Category.objects.all()
    return {'cats': cats}


@register.inclusion_tag('blog/main_menu.html', name='show_menu')
def show_main_menu(title = ''):
    
    menu = [{'title': 'home', 'url_name': 'home', 'is_selected': False},
            {'title': 'contacts', 'url_name': 'contacts', 'is_selected': False},
            # {'title': 'add post', 'url_name': 'add_post', 'is_selected': False},
            {'title': 'login', 'url_name': 'login', 'is_selected': False},
            {'title': 'register', 'url_name': 'register', 'is_selected': False},
            {'title': 'about', 'url_name': 'about', 'is_selected': False}]

   
    for i in menu:
        i['is_selected'] = True if i['title'] == title.lower() else False
    return {'menu': menu}


@register.inclusion_tag('blog/main_menu.html', name='show_menu_auth')
def show_main_menu_auth(title = '', username = ''):
    
    menu = [{'title': 'home', 'url_name': 'home', 'is_selected': False},
            {'title': 'contacts', 'url_name': 'contacts', 'is_selected': False},
            {'title': 'add post', 'url_name': 'add_post', 'is_selected': False},
            {'title': 'logout', 'url_name': 'logout', 'is_selected': False},
            {'title': f'{username}', 'url_name': 'home', 'is_selected': False},
            {'title': 'about', 'url_name': 'about', 'is_selected': False}]

   
    for i in menu:
        i['is_selected'] = True if i['title'] == title.lower() else False
    return {'menu': menu}
