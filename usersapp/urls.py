from django.urls import path

from usersapp import views


urlpatterns = [
    path('',views.home,name="home"),
    path('sign-up/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    

]
