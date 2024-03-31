from django.urls import path
from . import views

urlpatterns = [
path('', views.profile, name="profile"),
    path('login', views.Login, name="Login"),
    path('register', views.Register, name="Register"),
    path('page_login', views.page_login, name="page_login"),
    path('task', views.task, name="task"),
    path('add_blog', views.add_blog, name="add_blog"),

    path('sales', views.sales, name="sales"),
    path('gallery', views.gallery, name="Gallery"),
]