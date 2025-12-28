from rest_framework import serializers

from . import models
from .models import (
    UserProfile,
    CategoryList,
    CategoryDetail,
    Genre,
    Country,
    Director,
    Actor,
    Review,
    Rating,
    Favourite,
    History,
    FavouriteItem,
    Movie,
    MovieVideo, MovieFrame, ReviewLike
)






from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password',
                  'age', 'phone_number',  'date_registered')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }







class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields =  ['first_name', 'last_name', 'rating']

class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields =   '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields = [ 'id', 'category_name' ]

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields =  ['full_name',]
class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id','full_name']
class DirectorDetailSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format='%d-%m-%Y')
    director_movies = DirectorListSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = ['full_name', 'director_photo', 'bio', 'birth_date', 'director_movies']

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','genre_name']
class CategoryDetailSerializer(serializers.ModelSerializer):
    genre =  GenreListSerializer(many=True, read_only=True)
    class Meta:
        model = CategoryDetail
        fields =  [  'category_name' , 'genre' ]

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name',]



class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields =  [ 'genre_name',  ]

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'country_name')

class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    country = CountryListSerializer(many=True, read_only=True)
    genre = GenreNameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_poster', 'movie_name', 'year', 'country', 'genre']


class ActorSerializer(serializers.ModelSerializer):

     class Meta:
        model = Actor
        fields = ['full_name',]


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id','full_name']

class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movies = MovieListSerializer(many=True, read_only=True)
    birth_date = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Actor
        fields = ['id','full_name', 'actor_photo', 'bio', 'birth_date', 'actor_movies' ]




class CountryDetailSerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ('id', 'country_name', 'movies')
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_name',)



class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideo
        fields =  [ 'video_name', 'video']

class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = ['image',]


class RatingCreateSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = Rating
    class Meta:
        model = Rating
        fields =  ['user', 'stars', 'movie']
class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = Rating
    class Meta:
        model = Rating
        fields =  ['user', 'stars', 'created_date']


class ReviewCreateSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(
        queryset=MovieVideo.objects.all()
    )

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format='%d/%m/%Y  %H:%M')
    user = UserProfileReviewSerializer()

    class Meta:
        model = Review
        fields =  ['user','comment', 'parent', 'created_date']

class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%d-%m-%Y')
    country = CountrySerializer(many=True, read_only=True)
    director = DirectorSerializer(many=True, read_only=True)
    genre = GenreNameSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    movie_video = MovieVideoSerializer(many=True, read_only=True)
    frame = MovieFrameSerializer(many=True, read_only=True)
    ratings =  RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields =  [ 'movie_name', 'year', 'country', 'genre', 'director' ,
                    'movie_time', 'actors', 'movie_poster', 'trailer', 'director',
                    'description', 'movie_status', 'movie_video' , 'frame', 'ratings' , 'reviews', ]





class ReviewLikeSerializer(serializers.ModelSerializer):
    user = UserProfileReviewSerializer()
    class Meta:
        model = ReviewLike
        fields = ['user', 'movie']




class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'


class FavouriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteItem
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
