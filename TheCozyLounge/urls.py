from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name="store"),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register_view,name='register'),
    path('protected/',views.ProtectedView.as_view(),name='protected'),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('AboutUs/', views.about_us, name='about_us'),
]