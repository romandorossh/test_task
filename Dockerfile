
FROM centos:8

RUN yum install epel-release -y

RUN yum install python3 -y
# create root directory for our project in the container
RUN mkdir -p /opt/project

RUN mkdir -p /opt/project/scripts

COPY squirro /opt/project/squirro

COPY scripts /opt/project/scripts

# Install any needed packages specified in requirements.txt
WORKDIR /opt/project/squirro
RUN pip3 install -r requirements.txt

RUN python3 /opt/project/squirro/manage.py collectstatic --no-input

RUN pip3 install gunicorn

RUN chmod +x /opt/project/scripts/*

# expose the port 8000
EXPOSE 8000

WORKDIR /opt/project/

CMD if [ "$DJANGO_ENV" = "tests" ]; \
    then ./scripts/run_tests.sh;  \
    else ./scripts/start.sh; \
    fi
