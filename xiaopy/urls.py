from django.urls import path

from xiaopy import views
from xiaopy.views import UserListView

urlpatterns=[
    path('',views.hello,name='index'),
    path('hello',views.hello,name='index'),
    path('listall',views.listAllUser,name='listall'),
    path('httpPost',views.httpPost,name='httpPost'),
    path('httpWithHeader',views.httpWithHeader,name='httpWithHeader'),
    path('rest-get',UserListView.as_view(),name='rest-get'),
    path('rest2',UserListView.as_view(),name='rest2'),
]