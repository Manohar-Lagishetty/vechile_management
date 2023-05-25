from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
    path('home',views.home,name='home'),
    path('detailsadd/',views.detailsadd, name = 'detailsadd'),
    path('displaydetails/',views.vechile_list,name='displaydetails'),
    path('delete_data/<int:vehicle_number>',views.delete_data,name='delete_data'),
    path('editdetails/<int:vehicle_number>',views.update_data,name='update_data'),
    path('update_data/<int:vehicle_number>',views.editdetails,name='edit_data'),

]
