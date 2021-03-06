FROM python:3.8

ARG project_dir=/projects/

ADD flask/requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt
