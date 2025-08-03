from django.http import HttpResponse
#from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Article')

#def index(request,):
#    return render(
#        request,
#        'articles/index.html',
#        context={'Title': 'ARTICLEs'},
#    )
#    return HttpResponse('Article')
