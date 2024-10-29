from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogSite,name='list'),
    path('<int:pk>/',views.BlogDetail,name='detail'),
    path('new/',views.BlogCreate,name='create'),
    path('<int:pk>/edit/',views.BlogEdit,name='edit'),
    path('<int:pk>/delete/',views.BlogDelete,name='delete'),
]
