from django.urls import path
# importing the function from views

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create',views.create_form,  name='create-form'),
    path('update/<int:id>',views.update_info,name='update_info'),
    path('delete/<int:id>',views.delete_info,name='delete')
]
