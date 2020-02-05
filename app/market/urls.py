from django.conf.urls import url
from django.views.decorators.cache import cache_page

from .views import ItemRudView, ItemCreateView, ItemListView, Seeder, QuickSortAPI, MergeSortAPI

urlpatterns = [
    url(r'^item/(?P<slug>[-\w]+)/$', ItemRudView.as_view(), name='item-rud'),
    url(r'^item/$', ItemCreateView.as_view(), name='item-create'),
    url(r'^$', ItemListView.as_view(), name='item-list'),

    url(r'^seeder/$', Seeder, name='seeder'),

    url(r'^quick/$', QuickSortAPI.as_view(), name='item-list'),
    url(r'^merge/$', MergeSortAPI.as_view(), name='item-list'),

    # url whit buffer at 2 mins
    # url(r'^$', cache_page(2 * 60)(ItemListView.as_view()), name='item-list'),
    # url(r'^item/(?P<slug>[-\w]+)/$', cache_page(2 * 60)(ItemRudView.as_view()), name='item-rud'),

]
