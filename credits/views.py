from django.views.generic import TemplateView
from django.shortcuts import render
from retro.models import Link, Article, Category, Comment,User,Profile

# Create your views here.

class custom_mixin_kategorimenu(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = Link.objects.all()
        context['categories'] = Category.objects.all()
        context['users'] = User.objects.all()
        context['articles'] = Article.objects.all()
        context['comments'] = Comment.objects.all()
        context['profiles'] = Profile.objects.all()

        return context

class Credits(custom_mixin_kategorimenu, TemplateView):
    template_name = 'credits/credits.html'