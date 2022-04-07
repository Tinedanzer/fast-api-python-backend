FROM python:3.9.10-slim as base

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat supervisor && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir -p /var/log/supervisor

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.1 && \
    poetry config virtualenvs.in-project false && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root && \
    touch /tmp/worker_db_pid /tmp/worker_subtasks_pid /tmp/worker_default_pid

# COPY ./etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./etc/ /etc/
COPY ./alembic.ini ./
COPY ./app ./app/


FROM base as runner
ENTRYPOINT [ "/app/app/entry_point.sh" ]


FROM base as tester
RUN poetry install --no-root
COPY ./tests/ ./tests/
CMD /app/tests/run_tests.sh
