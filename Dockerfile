FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install django

RUN python3 manage.py migrate

RUN python3 manage.py createsuperuser

EXPOSE 80

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
