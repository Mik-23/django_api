from django.contrib.postgres.aggregates import ArrayAgg
from django.http import JsonResponse
from django.db.models import Q
from movies.models import Filmwork
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView


class MoviesListApi(BaseListView):
    model = Filmwork
    paginate_by = 50
    http_method_names = ['get']

    def get_queryset(self):
        return Filmwork.objects.all()

    def serialize_filmwork(self, filmwork):
        actors = []
        writers = []
        directors = []
        print(filmwork.persons.all())
        for person_filmwork in filmwork.personfilmwork_set.all():
            person = person_filmwork.person  # Получаем объект Person
            if person_filmwork.role == 'actor':
                actors.append(person.full_name)
            elif person_filmwork.role == 'writer':
                writers.append(person.full_name)
            elif person_filmwork.role == 'director':
                directors.append(person.full_name)
        return {
            'id': str(filmwork.id),  # Преобразование в строку, если это UUID
            'title': filmwork.title,
            'description': filmwork.description,
            'creation_date': filmwork.creation_date,
            'rating': filmwork.rating,
            'type': filmwork.type,
            'genres': [genre.name for genre in filmwork.genres.all()],
            'actors': actors,
            'directors': directors,
            'writers': writers,

        }

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, self.paginate_by)

        results = [self.serialize_filmwork(filmwork) for filmwork in queryset]

        return {
            'count': paginator.count,
            'results': results,
        }

    def render_to_response(self, context, **response_kwargs):
        print('LEN:', len(context["results"]))
        return JsonResponse(context)


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        return Filmwork.objects.all()

    def serialize_filmwork(self, filmwork):
        return {
            'id': str(filmwork.id),  # Преобразование в строку, если это UUID
            'title': filmwork.title,
            'description': filmwork.description,

        }

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, self.paginate_by)

        results = [self.serialize_filmwork(filmwork) for filmwork in queryset]

        return {
            'count': paginator.count,
            'results': results,
        }

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesDetailApi(BaseDetailView):
    model = Filmwork  # Модель
    http_method_names = ['get']

    def get_object(self, queryset=None):
        # Получает объект по переданному идентификатору (например, UUID)
        obj = super().get_object(queryset)
        return obj

    def render_to_response(self, context, **response_kwargs):
        # Преобразуем полученный объект в словарь и возвращаем его в ответе
        filmwork = self.get_object()
        actors = []
        writers = []
        directors = []
        print(filmwork.persons.all())
        for person_filmwork in filmwork.personfilmwork_set.all():
            person = person_filmwork.person  # Получаем объект Person
            if person_filmwork.role == 'actor':
                actors.append(person.full_name)
            elif person_filmwork.role == 'writer':
                writers.append(person.full_name)
            elif person_filmwork.role == 'director':
                directors.append(person.full_name)
        return JsonResponse({
            'id': str(filmwork.id),  # Преобразование в строку, если это UUID
            'title': filmwork.title,
            'description': filmwork.description,
            'creation_date': filmwork.creation_date,
            'rating': filmwork.rating,
            'type': filmwork.type,
            'genres': [genre.name for genre in filmwork.genres.all()],
            'actors': actors,
            'directors': directors,
            'writers': writers,

        })