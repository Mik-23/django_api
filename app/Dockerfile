FROM python:3.12

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'example.settings'


COPY requirements.txt requirements.txt


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir -p /opt/app/movies/static/
RUN mkdir -p /opt/app/movies/media/


COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]