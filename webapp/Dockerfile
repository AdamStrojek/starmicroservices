FROM python:3.7-alpine

MAINTAINER Adam Strojek <adam@strojek.info>

RUN apk add --upgrade --no-cache \
    bash \
    curl \
    freetype-dev \
    gettext \
    libjpeg \
    libstdc++ \
    py-pip && \
    apk add --no-cache --virtual .build-dependencies \
    build-base \
    jpeg-dev \
    libffi-dev \
    linux-headers \
    freetype-dev \
    python-dev \
    zlib-dev

RUN pip install --upgrade pip && pip install wheel==0.32.3

# This can be usefull later when database connection will be added
# ENV WAITFORIT_VERSION="v2.4.1"
# RUN curl -o /usr/local/bin/waitforit -sSL https://github.com/maxcnunes/waitforit/releases/download/$WAITFORIT_VERSION/waitforit-linux_amd64 && \
#     chmod +x /usr/local/bin/waitforit

WORKDIR /usr/src/app

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

RUN apk del .build-dependencies

COPY . .

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5050" ]
