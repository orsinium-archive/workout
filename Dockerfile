FROM python:3.7-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./workout/           /opt/project/workout
COPY ./setup.py           /opt/project/
COPY ./requirements.txt   /opt/project/

WORKDIR /opt/project
RUN pip install -U pip tox
RUN pip install -e .

ENV DJANGO_SETTINGS_MODULE "workout.settings"
ENTRYPOINT ["workout"]
CMD ["runserver", "0.0.0.0:1337"]
