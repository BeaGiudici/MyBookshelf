from python:3.13

WORKDIR /MyBookshelf

COPY ./requirements.txt /MyBookshelf/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /MyBookshelf/requirements.txt

COPY ./app /MyBookshelf/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
