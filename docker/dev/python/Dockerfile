FROM python:3.7-alpine

ARG requirements=requirements/dev.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY ./src /src

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN pip install --no-cache-dir -r ${requirements}

ENTRYPOINT ["/entrypoint.sh"]