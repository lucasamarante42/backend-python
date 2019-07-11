from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/clients/(?P<pk>[0-9]+)$', # Url to get update or delete a clients
        views.get_delete_update_client.as_view(),
        name='get_delete_update_client'
    ),
    path('api/v1/clients/', # urls list all and create new one
        views.get_post_clients.as_view(),
        name='get_post_clients'
    )
]
