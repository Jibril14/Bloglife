from django.urls import path
from . import views
urlpatterns = [
    path('latest', views.index, name="home-page"),
    path('about', views.about_page, name="about-page"),
    path('latest/<slug:slug>', views.single_post, name="post-detail")
]
