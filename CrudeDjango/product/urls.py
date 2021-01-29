from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name='index'), 
    path('',views.show,name='show'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('delete/<int:id>/',views.delete_data ,name='delete'),
    path('confirmdelete',views.confirm_delete,name="confrimdelete"),
    path('update/<int:id>/',views.update,name="update")
]
