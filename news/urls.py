from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView, name="home"),
    path('all_news/', AllNewsView.as_view(), name="all-news"),
    path('category/<int:id>', CategoryView, name="category-news"),
    path('region/<int:id>', RegionView, name="region-news"),
    path('detail/<int:id>', DetailView, name="detail"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


