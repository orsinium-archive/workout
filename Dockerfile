FROM python:3.7-alpine

WORKDIR /opt/project
RUN pip install -e .

ENTRYPOINT ["workout"]
RUN ["runserver"]
