from django.urls import path
from news.views import home, NewslistView , NewsDetailView
urlpatterns = [
    path('', NewslistView.as_view(), name="home")
]
