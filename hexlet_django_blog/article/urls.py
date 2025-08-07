from django.urls import path
#from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, index, ArticleView

app_name = 'articles'

urlpatterns = [
    path('', IndexView.as_view()),
    path('<str:tags>/<int:article_id>', index, name='article'),
    path('<int:pk>/', ArticleView.as_view(), name='article_show')
]
