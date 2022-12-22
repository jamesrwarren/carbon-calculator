FROM python:3.9

RUN mkdir -p /opt/application/flask
COPY project /opt/application/flask/project
COPY requirements.txt /opt/application/flask/requirements.txt
WORKDIR /opt/application/flask

RUN apt-get update
RUN pip install -r requirements.txt
ENV DATABASE_HOST postgres-db

ENV PYTHONPATH=/opt/application/flask
# ENTRYPOINT ["gunicorn", "--reload", "--workers=1", "--threads=1", "-b", ":8088"]
# CMD ["project.app:create_app()"]
ENV FLASK_APP=/opt/application/flask/project/app.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]