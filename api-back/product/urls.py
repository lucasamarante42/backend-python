from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/products/(?P<pk>[0-9]+)$', # Url to get update or delete a products
        views.get_delete_update_product.as_view(),
        name='get_delete_update_product'
    ),
    path('api/v1/products/', # urls list all and create new one
        views.get_post_products.as_view(),
        name='get_post_products'
    )
]
