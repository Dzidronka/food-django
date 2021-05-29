from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from .views import SearchResultsView

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^product/(?P<pk>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^product/new/$', views.product_add, name='product_add'),
    url(r'^product/(?P<pk>\d+)/edit/$', views.product_edit, name='product_edit'),
    url(r'^product/(?P<pk>\d+)/publish/$', views.product_publish, name='product_publish'),
    url(r'^product/(?P<pk>\d+)/remove/$', views.product_remove, name='product_remove'),
    url(r'^product/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^search/$', SearchResultsView.as_view(), name='search_results'),
    url(r'^product-add/$', views.product_add, name='product_add'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
