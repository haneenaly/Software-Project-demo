from django.urls import path
from .views import index 

# define a list of url patterns
#path of the app 
urlpatterns = [
    path('', index, name="index"),
]