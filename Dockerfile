# Use an official Python runtime as a parent image
FROM python:3.8-bullseye
LABEL maintainer="hello@wagtail.org"

# Set environment varibles
ENV PYTHONUNBUFFERED 1

# Install libenchant and create the requirements folder.
RUN apt-get update -y \
    && apt-get install -y libenchant-2-dev postgresql-client \
    && mkdir -p /code/requirements

# Install the wagtailtables_demo project's dependencies into the image.
COPY ./wagtailtables_demo/requirements.txt /code/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade pip \
    && pip install -r /code/requirements.txt

# Install wagtailtables from the host. This folder will be overwritten by a volume mount during run time (so that code
# changes show up immediately), but it also needs to be copied into the image now so that wagtailtables can be pip install'd.
RUN mkdir /code/wagtailtables
COPY ./wagtailtables /code/wagtailtables/wagtailtables
COPY ./setup.py /code/wagtailtables/
COPY ./README.md /code/wagtailtables/

RUN cd /code/wagtailtables/ \
    && pip install -e .