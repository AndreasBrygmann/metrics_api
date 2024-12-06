FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 80
RUN chmod +x metrics_api
CMD ["metrics_api", "run", "app/main.py", "--port", "80"]