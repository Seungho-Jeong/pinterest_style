FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Seungho-Jeong/pinterest_style.git

WORKDIR /home/pinterest_style/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY = 'django-insecure-f_2sbl5+rcjp^oqpweq3#ezq)lca4f3hx%no#=0(#0a=pal5*6'" > my_settings.py

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "--bind", "0:8000"]