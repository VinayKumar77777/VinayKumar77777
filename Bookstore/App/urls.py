from django.urls import path
from . import views

urlpatterns = [
    path("",views.base,name='base'),
    path("homepage/",views.Homepage,name='homepage'),
    path("addbook/",views.Addbook,name='addbook'),
    path("edit/<int:id>",views.Edit,name='edit'),
    path("delete/<int:id>",views.Delete,name='delete'),
    path("viewdetails/<int:id>",views.viewdetails,name='viewdetails'),
    path("search/",views.search,name='search'),
] 
