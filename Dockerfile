FROM python:3.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN chown -R node /app/main.py


COPY ./app /code/app

EXPOSE 80


CMD ["metrics_api", "run", "app/main.py", "--port", "80"]
