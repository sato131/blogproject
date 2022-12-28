from django.urls import path
from .views import Bloglist, Blogdetail, Blogcreate, Blogdelete, Blogupdate

urlpatterns = [
    path('list/', Bloglist.as_view(), name='list'),
    path('detail/<int:pk>/', Blogdetail.as_view(), name='detail'),
    path('create/', Blogcreate.as_view(), name='create'),
    path('delete/<int:pk>/', Blogdelete.as_view(), name='delete'),
    path('update/<int:pk>/', Blogupdate.as_view(), name='update'),
]