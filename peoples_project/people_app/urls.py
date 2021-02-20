from django.urls import path
from . import views


urlpatterns=[
    #path('',views.index,name="index"),
    path('',views.show,name="show"),
    path('addpeople',views.add_people,name="addpeople"),
    path('updatepeople/<int:id>/',views.update_people,name="updatepeople"),
    path('deletepeople/<int:id>/',views.delete_people,name="deletepeople")
]