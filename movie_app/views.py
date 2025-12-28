from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, permissions, status
from .models import  ( UserProfile, CategoryList, CategoryDetail, Genre, Country,
                        Director, Actor, Movie, MovieVideo, MovieFrame, Rating,
                        Review, ReviewLike, Favourite, FavouriteItem, History )
from .serializers import (MovieListSerializer, MovieDetailSerializer, CategoryListSerializer, CategoryDetailSerializer,
                          GenreListSerializer, CountryDetailSerializer,
                          DirectorDetailSerializer, DirectorListSerializer, ActorDetailSerializer,
                          ActorListSerializer, MovieVideoSerializer, GenreDetailSerializer,
                          UserProfileSerializer, ReviewCreateSerializer, RatingCreateSerializer,
                          FavouriteItemSerializer,
                          FavouriteSerializer, HistorySerializer, CountryListSerializer, ReviewLikeSerializer,
                          UserRegisterSerializer, UserLoginSerializer
                          )
from .permissions import UserStatusPermission, CreatePermission
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class =  UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated, CreatePermission]


class ReviewLikeViewSet(viewsets.ModelViewSet):
    queryset = ReviewLike.objects.all()
    serializer_class = ReviewLikeSerializer
class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingCreateSerializer
    permission_classes = [permissions.IsAuthenticated, CreatePermission]

class FavouriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavouriteItem.objects.all()
    serializer_class = FavouriteItemSerializer
class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

class GenreMoviesAPIView(generics.ListAPIView):
        queryset = Genre.objects.all()
        serializer_class = MovieListSerializer
        filter_backends = [DjangoFilterBackend,]
        filter_fields = ['genre']
class CategoryListAPIView( generics.ListAPIView ):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category']
class CategoryDetailAPIView( generics.RetrieveAPIView ):
    queryset = CategoryDetail.objects.all()
    serializer_class = CategoryDetailSerializer


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = [UserStatusPermission]

class GenrelistAPIView( generics.ListAPIView ):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
class GenreDetailAPIView( generics.RetrieveAPIView ):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer
    filter_backends = [DjangoFilterBackend,]
class CountryDetailAPIView( generics.RetrieveAPIView ):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
class CountryListAPIView( generics.ListAPIView ):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer
    filter_backends = [DjangoFilterBackend,]
class ActorListAPIView( generics.ListAPIView ):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer
class ActorDetailAPIView( generics.RetrieveAPIView ):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
class MovieVideoViewSet(viewsets.ModelViewSet):
    queryset = MovieVideo.objects.all()
    serializer_class = MovieVideoSerializer
class MovieFrameViewSet(viewsets.ModelViewSet):
     queryset = MovieFrame.objects.all()
     serializer_class = MovieVideoSerializer
class  DirectorListAPIView( generics.ListAPIView ):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializer
class DirectorDetailAPIView( generics.RetrieveAPIView ):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer