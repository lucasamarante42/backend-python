from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/stocks/(?P<pk>[0-9]+)$', # Url to get update or delete a stocks
        views.get_delete_update_stock.as_view(),
        name='get_delete_update_stock'
    ),
    path('api/v1/stocks/', # urls list all and create new one
        views.get_post_stocks.as_view(),
        name='get_post_stocks'
    )
]
