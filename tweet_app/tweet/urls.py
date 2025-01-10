from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.tweet_list, name="tweet_list"),
    path("create/", views.create_tweet, name="create_tweet"),
    path("<int:tweet_id>/delete/", views.delete_tweet, name="delete_tweet"),
    path("<int:tweet_id>/edit/", views.edit_tweet, name="edit_tweet"),

    path("__reload__/", include("django_browser_reload.urls")),

] 
