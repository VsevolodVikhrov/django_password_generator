FROM python:3.8

ENV DEBIAN_FRONTEND=noninteractive
ADD . /opt/generator/
WORKDIR opt/generator/

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

ENTRYPOINT ["./manage.py", "runserver"]