from django.urls import path
from . import views


urlpatterns = [

    # HOME
    path(
        '',
        views.home,
        name='home'
    ),

    # AUTHENTICATION
    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    # ITEMS
    path(
        'item/add/',
        views.item_create,
        name='item_create'
    ),

    path(
        'item/<int:pk>/',
        views.item_detail,
        name='item_detail'
    ),

    path(
        'item/<int:pk>/edit/',
        views.item_update,
        name='item_update'
    ),

    path(
        'item/<int:pk>/delete/',
        views.item_delete,
        name='item_delete'
    ),
]