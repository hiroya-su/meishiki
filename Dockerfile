FROM python:3
USER root

ARG project_dir=/root/src/
ADD requirements.txt $project_dir
WORKDIR $project_dir
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

