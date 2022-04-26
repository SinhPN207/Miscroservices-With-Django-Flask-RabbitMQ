from django.urls import path

from .views import ProductViews, UserAPIView

urlpatterns = [
    path('products', ProductViews.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViews.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('user', UserAPIView.as_view())
]
