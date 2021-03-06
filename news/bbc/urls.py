from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'v1', views.NewsApiViews)


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('news-details/<slug>', views.news_details, name='news-details'),
    path('cat-list/<cat_id>', views.cat_list, name='cat-list'),

    path('news-search', views.news_search, name='news-search'),
    path('contact', views.contact, name='contact'),
    path('api/', include(router.urls))

]
