from django.conf.urls import url

from .views import ItemRudView, ItemCreateView, ItemListView, Seeder, QuickSortAPI, MergeSortAPI, Salute

urlpatterns = [
    url(r'^item/(?P<slug>[-\w]+)/$', ItemRudView.as_view(), name='item-rud'),
    url(r'^item/$', ItemCreateView.as_view(), name='item-create'),
    url(r'^$', ItemListView.as_view(), name='item-list'),
    url(r'^salute/$', Salute.as_view(), name='item-list'),

    url(r'^seeder/$', Seeder, name='seeder'),

    url(r'^quick/$', QuickSortAPI.as_view(), name='item-list'),
    url(r'^merge/$', MergeSortAPI.as_view(), name='item-list'),

]
