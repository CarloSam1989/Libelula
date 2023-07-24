from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.ver_productode, name='ver_producto'),
    path('productos/', views.view_producto, name="productos"),
    path('addproductos/',views.add, name='registrar_producto'),
    path('addcategoria/',views.addcategoria, name='registrar_categoria'),
    path('register/',views.registrar, name='register'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
    path('login/',LoginView.as_view(template_name='tienda/login.html'),name='login'),
    #path('logout/',LogoutView.as_view(template_name='tienda/logout.html'),name='logout'),

]

