from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/client_addresses/(?P<pk>[0-9]+)$', # Url to get update or delete a clients addresses
        views.get_delete_update_client_addresses.as_view(),
        name='get_delete_update_client_addresses'
    ),
    path('api/v1/client_addresses/', # urls list all and create new one
        views.get_post_client_addresses.as_view(),
        name='get_post_client_addresses'
    )
]
