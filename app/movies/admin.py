from django.contrib import admin
from .models import *
# Register your models here.


class PersonFilmWorkInline(admin.TabularInline):
    model = PersonFilmwork
    extra = 1  # Количество пустых форм для добавления новых записей

class GenreFilmWorkInline(admin.TabularInline):
    model = GenreFilmwork
    extra = 1

class FilmWorkAdmin(admin.ModelAdmin):
    inlines = [PersonFilmWorkInline, GenreFilmWorkInline]  # Включаем инлайн для персонажей
    filter_horizontal = ('genres', 'persons')  # Удобный выбор жанров
    list_display = ('Название', 'Описание', 'Дата создания', 'Рейтинг', 'Тип', 'Создан', 'Изменён')
    search_fields = ('Название', 'Описание', 'Дата создания', 'Рейтинг', 'Тип', 'Создан', 'Изменён')
    list_filter = ('genres', 'persons')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('Название', 'Описание', 'Создан', 'Изменён')
    search_fields = ('Название', 'Описание', 'Создан', 'Изменён')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('Полное имя', 'Создал', 'Изменил')
    search_fields = ('Полное имя', 'Создал', 'Изменил')

admin.site.register(Filmwork)
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(GenreFilmwork)
admin.site.register(PersonFilmwork)
