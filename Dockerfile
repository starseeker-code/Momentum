FROM python:3.10.17-alpine3.21

LABEL MAINTAINER="Joaquin Hernandez Martinez <proyecto_noether@outlook.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD . /var/www/
RUN poetry install
RUN poetry shell

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD ["flask", "run", "--debug"]
#CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]