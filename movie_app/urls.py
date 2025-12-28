from django.urls import path, include

from django.contrib import admin
from .models import Movie, Genre, Country, Director

from rest_framework.routers import DefaultRouter
from .views import (MovieListAPIView, MovieDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, GenrelistAPIView,
                    GenreDetailAPIView,
                    ActorListAPIView, ActorDetailAPIView,
                    CountryListAPIView, CountryDetailAPIView, UserViewSet, ReviewLikeViewSet, RatingCreateAPIView,
                    FavouriteItemViewSet, FavouriteViewSet, ReviewCreateAPIView,
                    HistoryViewSet, DirectorListAPIView, DirectorDetailAPIView, RegisterView, LoginView, LogoutView
                    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'review', ReviewLikeViewSet)
router.register(r'favourites', FavouriteViewSet)
router.register(r'favourites', FavouriteItemViewSet)
router.register(r'history',  HistoryViewSet)





urlpatterns = [
    path ('', include(router.urls)),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path ('genre/', GenrelistAPIView.as_view(), name='genre_list'),
    path( r'genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path( r'movies/', MovieListAPIView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('accounts/', include('allauth.urls')),
    path('countries/', CountryListAPIView.as_view(), name='country_list'),
    path('countries/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('directors/', DirectorListAPIView.as_view(), name='director_list'),
    path('directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actors/', ActorListAPIView.as_view(), name='actor_list'),
    path('actors/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('ratings/', RatingCreateAPIView.as_view(), name='rating_create'),
    path('reviews/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),



]

