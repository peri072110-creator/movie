from django.contrib import admin

from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin



class GenreInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Genre
    extra = 1



@admin.register(CategoryList )
class CategoryAdmin( TranslationAdmin ):

    inlines = [GenreInline]
    class Meta:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),

        }

class MovieVideoInline(admin.TabularInline):
    model = MovieVideo
    extra = 1
class MovieFrameInline(TranslationAdmin):
    model = MovieFrame
    extra = 1

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    search_fields = ('full_name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ('country_name',)
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ('full_name',)
@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    inlines = [MovieVideoInline,]


admin.site.register(UserProfile)

admin.site.register(MovieFrame)

admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Favourite)
admin.site.register(FavouriteItem)
admin.site.register(History)




