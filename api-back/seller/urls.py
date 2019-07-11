from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/sellers/(?P<pk>[0-9]+)$', # Url to get update or delete a sellers
        views.get_delete_update_seller.as_view(),
        name='get_delete_update_seller'
    ),
    path('api/v1/sellers/', # urls list all and create new one
        views.get_post_sellers.as_view(),
        name='get_post_sellers'
    )
]
