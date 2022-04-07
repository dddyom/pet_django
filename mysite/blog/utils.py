from .models import *


class DataMixin:

    model = Blog
    template_name = 'blog/index.html'

    context_object_name = 'posts'
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        return context


