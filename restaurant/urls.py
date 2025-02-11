from django.urls import path
from restaurant import views
urlpatterns=[
    path("",views.hello),
    path("home/",views.mainpage,name="home"),
    path("reviews/",views.reviewlist,name="reviews"),
    path("dishes/",views.dishlist,name="dishes"),
    path("dishdetail/<slug:slug>",views.dishdetail,name="dishdetail")
    
]
