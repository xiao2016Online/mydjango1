from django.urls import path

from xiaopy import views
from xiaopy.views import UserListView

urlpatterns=[
    # path('',views.hello,name='index'),
    path('hello',views.hello,name='index'),
    path('httpPost',views.httpPost,name='httpPost'),
    path('httpWithHeader',views.httpWithHeader,name='httpWithHeader'),
    path('rest-get',UserListView.as_view(),name='rest-get'),
    path('list',views.listAllUser,name='list'),
    path('detail/<pk>',views.UserDetailView.as_view(),name='detail'),
    path('detail',views.UserDetail.as_view(),name='detail'),
]