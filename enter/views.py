from .models import *
from django.views.generic import TemplateView, ListView
class Mainopen(TemplateView):
    template_name = 'index.html'
class Table(ListView):
    model = Post
    template_name = 'tablepupil.html'
    context_object_name = 'object_post'