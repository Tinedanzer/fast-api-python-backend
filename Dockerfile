FROM python:3.9.10-slim as base

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.2 && \
    poetry config virtualenvs.in-project false && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

COPY ./alembic.ini ./
COPY ./app ./app/


FROM base as runner
CMD sleep 5 && \
    poetry run alembic upgrade head && \
    poetry run uvicorn --host=0.0.0.0 app.main:fast_app --reload --reload-dir /app/app/


FROM base as tester
RUN poetry install --no-root
COPY ./tests/ ./tests/
CMD /app/tests/run_tests.sh
