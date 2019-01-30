FROM python:3.7-alpine

COPY ./workout/           /opt/project/workout
COPY ./setup.py           /opt/project/
COPY ./requirements.txt   /opt/project/

WORKDIR /opt/project
RUN pip install -U pip
RUN pip install -e .

ENTRYPOINT ["workout"]
CMD ["runserver"]
