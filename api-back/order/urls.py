from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/orders/(?P<pk>[0-9]+)$', # Url to get update or delete a orders
        views.get_delete_update_orders.as_view(),
        name='get_delete_update_orders'
    ),
    path('api/v1/orders/', # urls list all and create new one
        views.get_post_orders.as_view(),
        name='get_post_orders'
    ),
    re_path(r'^api/v1/orders-to-pdf/(?P<pk>[0-9]+)$', # Url to get update or delete a orders
        views.get_orders_to_pdf.as_view(),
        name='get_orders_to_pdf'
    )
]
