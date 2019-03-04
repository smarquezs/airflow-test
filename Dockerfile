FROM python:3.6.3
# supervisord setup

RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Airflow setup
#
ENV SLUGIFY_USES_TEXT_UNIDECODE=yes
ENV AIRFLOW_HOME=/app/airflow

RUN pip install psycopg2
RUN pip install apache-airflow

RUN airflow initdb

WORKDIR $AIRFLOW_HOME

EXPOSE 8080

