from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import Category

# Create your views here.



class HomeView(View):
    def get(self, request):
        category_list = Category.objects.all()
        return render(request, 'blog/home.html', {'categories': category_list})



class CategoryView(View):
    """Вывод статей категории"""
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, 'blog/posts_list.html', {'category': category})
