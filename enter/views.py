from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.views.generic import TemplateView, ListView
from .form import *
class Mainopen(TemplateView):
    template_name = 'index.html'
class Table(ListView):
    model = Post
    template_name = 'tablepupil.html'
    context_object_name = 'object_post'
# class Starter(TemplateView):
#     template_name = 'forms/form_my_form.html'

def blog_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Siz muvafaqiyatli Ro`yxatdan O`tdingiz')
            return redirect("maindir")
    else:
        form = BlogForm
    return render(request, 'forms/form_my_form.html' ,{'form':form})

