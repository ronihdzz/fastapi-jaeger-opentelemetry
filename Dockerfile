FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV ROOT_PATH=/
ENV PORT=9000

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libpq-dev \
    postgresql-dev \
    && pip install --upgrade pip \
    && pip install gunicorn uvicorn[standard]

WORKDIR /application/src

COPY ./requirements_with_versions.txt /application/
RUN pip install --no-warn-script-location --disable-pip-version-check --no-cache-dir -r /application/requirements_with_versions.txt

COPY ./src /application/src
EXPOSE $PORT

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT --root-path $ROOT_PATH"] 