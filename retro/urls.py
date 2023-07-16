
from urllib import request
from . import views
from django.urls import path
from .views import Index, Links,Contact, About, Kategories, Thankyou, Test, Edit_profile, View_profile,List_Users,article_detail,articles_by_category,articles_by_author,create_article

#app_name = "retro"

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('links', Links.as_view(), name='links'),
    path('contact',Contact.as_view(), name='contact'),
    path('about', About.as_view(), name='about'),
    path('category', Kategories.as_view(), name='Kategories'),
    path('create_article', create_article, name='create_article'),
    path('test', Test.as_view(), name='test'),
    path('thankyou', Thankyou.as_view(), name='thankyou'),
    path('edit_profile', Edit_profile.as_view(), name='edit_profile'),
    path("view_profile", View_profile.as_view(), name='view_profile'),
    path('list_users', List_Users.as_view(), name='list_users'),
    path("article/<int:pk>/", article_detail.as_view(), name="article_detail"),
    path("category/<int:pk>/", articles_by_category.as_view(), name="articles_by_category"),
    path("author/<int:pk>/", articles_by_author.as_view(), name="articles_by_author"),
    ]