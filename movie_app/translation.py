from phonenumbers.unicode_util import Category

from .models import CategoryList, CategoryDetail,  Genre, Country, Director, Actor, Movie, MovieVideo
from modeltranslation.translator import TranslationOptions,register




@register(CategoryList)
class CategoryTranslationOptions(TranslationOptions):
    fields = ( 'category_name',)


@register(CategoryDetail)
class CategoryDetailTranslationOptions(TranslationOptions):
    fields = ( 'category_name',)

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ( 'genre_name',)
@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ( 'country_name',)
@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ( 'full_name', 'bio')
@register(Actor)
class  ActorTranslationOptions(TranslationOptions):
    fields = ( 'full_name', 'bio')

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = (  'movie_name', 'description',)
@register(MovieVideo)
class MovieVideoTranslationOptions(TranslationOptions):
    fields = ( 'video_name', )

