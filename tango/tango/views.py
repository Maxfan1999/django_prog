from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app.models import Article


def main_page(request):
    context = RequestContext(request)
    articles = Article.objects.all()
    context_dir = {'articles' : articles}
    return render(request,'main.html',context_dir,context)