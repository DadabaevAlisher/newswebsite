from django.shortcuts import render
from requests import request
from .models import *
from django.views.generic import ListView
# Create your views here.


def HomeView(request):
    latest_news = News.objects.all().order_by('-id')[1:2]
    other_news = News.objects.all().order_by('-id')[1:12]
    categories = Category.objects.all()
    regions = Region.objects.all()
    context = {
        'latest_news': latest_news,
        'other_news': other_news,
        'categories': categories,
        'regions': regions
    }
    return render(request, 'home.html', context)


def DetailView(request, id):
    news = News.objects.get(id=id)
    category = Category.objects.get(id=news.catogory.id)
    rel_news = News.objects.filter(catogory=category).exclude(id=id)
    context = {
        'news': news,
        'category': category,
        'rel_news': rel_news
    }
    return render(request, 'detail.html', context)


class AllNewsView(ListView):
    model = News
    template_name = 'all-news.html'


def CategoryView(request, id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(catogory=category)

    return render(request, 'cotegory_news.html', {
        'news': news,
        'category': category
        })


def RegionView(request, id):
    region = region.objects.get(id=id)
    news = News.objects.filter(catogory=region)

    return render(request, 'region_news.html', {
        'news': news,
        'region': region
        })



