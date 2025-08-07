#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
#from django.shortcuts import redirect
#from django.views.decorators.http import require_http_methods
from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={'articles': articles})

#    def get(self, request, *args, **kwargs):
#       url = reverse("article", kwargs={'tags': 'python', 'article_id': 42})
#        return redirect(url)

def index(request, tags, article_id):
    return render(
        request,
        'articles/index.html',
        context={'Title': 'ARTICLEs', 'Tags': tags, 'Article_id': article_id},
    )

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        return render(request, "articles/show.html", context={'article': article})
