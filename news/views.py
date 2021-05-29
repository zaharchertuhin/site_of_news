from django.shortcuts import render
from news.models import News
from django.views.generic import ListView, DetailView

class NewslistView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"

class NewsDetailView(DetailView):
    model = News
    context_object_name = News

def home(request):
    # value = 0
    return render(request, "news/news_list.html")
