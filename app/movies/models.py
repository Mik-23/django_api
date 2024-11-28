import uuid
from django.db import models

# Create your models here.


class Genre(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.TextField("Название")
    description = models.TextField("Описание", null=True)
    created = models.DateTimeField("Создан", auto_now_add=True)
    modified = models.DateTimeField("Изменён", auto_now=True)
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        managed = False
        db_table = 'genre'
class Person(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    full_name = models.TextField("Полное имя")
    created = models.DateTimeField("Создал", auto_now_add=True)
    modified = models.DateTimeField("Изменил", auto_now=True)
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        managed = False
        db_table = 'person'

class Filmwork(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    title = models.TextField("Название")
    description = models.TextField("Описание")
    creation_date = models.DateField("Дата создания")
    rating = models.FloatField("Рейтинг")
    type = models.TextField("Тип")
    created = models.DateTimeField("Создан", auto_now_add=True)
    modified = models.DateTimeField("Изменён", auto_now=True)
    genres = models.ManyToManyField(Genre, through='GenreFilmWork', related_name='films')
    persons = models.ManyToManyField(Person, through='PersonFilmWork', related_name='films')
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        managed = False
        db_table = 'film_work'


class GenreFilmwork(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE)
    film_work = models.ForeignKey(
        Filmwork, on_delete=models.CASCADE)
    created = models.DateTimeField("Создан", auto_now_add=True)
    class Meta:
        verbose_name = 'Жанр фильма'
        verbose_name_plural = 'Жанры фильмов'
        managed = False
        db_table = 'genre_film_work'

class PersonFilmwork(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    film_work = models.ForeignKey(
        Filmwork, on_delete=models.CASCADE)
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE)
    role = models.TextField("Роль")  # Необходимо добавить круглые скобки, чтобы это было полем модели
    created = models.DateTimeField("Создал", auto_now_add=True)

    class Meta:
        verbose_name = 'Участник фильма'
        verbose_name_plural = 'Участники фильмов'
        managed = False
        db_table = 'person_film_work'
