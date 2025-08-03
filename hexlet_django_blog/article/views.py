#from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect
#from django.views.decorators.http import require_http_methods

class IndexView(View):
    def get(self, request, *args, **kwargs):
        url = reverse("article", kwargs={'tags': 'python', 'article_id': 42})
        return redirect(url)

def index(request, tags, article_id):
    return render(
        request,
        'articles/index.html',
        context={'Title': 'ARTICLEs', 'Tags': tags, 'Article_id': article_id},
    )

