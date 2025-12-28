from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import  MinValueValidator, MaxValueValidator

StatusChoices = (
    ('pro', 'pro'),
    ('simple', 'simple'),
)

class UserProfile(AbstractUser):
    phone_number =  PhoneNumberField(null=True, blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(70)],null=True, blank=True)
    user_photo = models.ImageField(upload_to="user_photo", null=True, blank=True)
    status = models.CharField(max_length=10, choices=StatusChoices, default='simple')
    date_registered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  f'{self.first_name}, {self.last_name}'

class CategoryList(models.Model):
   category_name = models.CharField(max_length=20, unique=True)
   description = models.TextField(blank=True)

   def __str__(self):
       return self.category_name
class CategoryDetail(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.category_name
class Genre(models.Model):
   genre_name = models.CharField(max_length=30)
   category = models.ForeignKey(CategoryList, on_delete=models.CASCADE, related_name='genre')
   def __str__(self):
       return  f'{self.genre_name}, {self.category}'

class Country(models.Model):
   country_name = models.CharField(max_length=100, unique=True)

   def __str__(self):
       return self.country_name

class Director(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='FIO')
    director_photo = models.ImageField(upload_to="director_photo" )
    birth_date = models.DateField()
    bio = models.TextField()
    def __str__(self):
        return self.full_name

class Actor(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='FIO')
    actor_photo = models.ImageField(upload_to="actor_photo")
    birth_date = models.DateField()
    bio = models.TextField()
    def __str__(self):
        return self.full_name


class Movie(models.Model):
     movie_name = models.CharField(max_length=100)
     year = models.DateField()
     country = models.ManyToManyField(Country, related_name='movies')
     director = models.ManyToManyField(Director, related_name='director_movies')
     genre = models.ManyToManyField(Genre)
     MovieTypeChoices = (
     ('360p', '360p'),
     ('480p', '480p'),
     ('720p', '720p'),
     ('1080p', '1080p'),
     ('1080p Ultra', '1080p Ultra'),
     )

     movie_type = models.CharField(max_length=20, choices=MovieTypeChoices)
     movie_time = models.PositiveIntegerField()
     actors = models.ManyToManyField(Actor, related_name='actor_movies')
     movie_poster = models.ImageField(upload_to="movie_poster")
     trailer = models.URLField()
     description = models.TextField()
     movie_status=models.CharField(max_length=10 , choices=StatusChoices)
     def __str__(self):
         return self.movie_name

class MovieVideo(models.Model):
   video_name = models.CharField(max_length=100, verbose_name='озвучка')
   video= models.FileField(upload_to="movie_video")
   movie= models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_video')

   def __str__(self):
       return  f'{self.video_name}, {self.movie}'


class MovieFrame(models.Model):
   image = models.ImageField(Movie, upload_to="movie_images")
   movie = models.ForeignKey(MovieVideo, on_delete=models.CASCADE, related_name='frames')

def __str__(self):
    return  f"{self.movie}, {self.image}"
class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(choices=[(i,str())for i in range(1,11)])
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.movie}, {self.user}, {self.stars}, {self.created_date}'

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieVideo, on_delete=models.CASCADE, related_name='reviews')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f' {self.user} '
class ReviewLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieVideo, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f' {self.user} '
class Favourite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
class FavouriteItem(models.Model):
    movie = models.ForeignKey(Favourite, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.movie} '
class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} , {self.movie}, {self.created_date}'