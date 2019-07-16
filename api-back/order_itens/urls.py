from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/orders_itens/(?P<pk>[0-9]+)$', # Url to get update or delete a orders itens
        views.get_delete_update_orders_itens.as_view(),
        name='get_delete_update_orders_itens'
    ),
    path('api/v1/orders_itens/', # urls list all and create new one
        views.get_post_orders_itens.as_view(),
        name='get_post_orders_itens'
    ),
    re_path(r'^api/v1/orders_itens_by_order/(?P<order_id>[0-9]+)$', # Url to get a orders itens
        views.get_orders_itens_by_order_id.as_view(),
        name='get_orders_itens_by_order_id'
    ),
]
