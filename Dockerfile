FROM python:3.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app

COPY ./static /code/static

EXPOSE 80


CMD ["metrics_api", "run", "app/main.py", "--port", "80"]