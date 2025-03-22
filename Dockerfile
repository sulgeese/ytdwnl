FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /ytdwnl

RUN pip install poetry && \
    poetry config virtualenvs.create false

ADD poetry.lock pyproject.toml ./

RUN poetry install --no-interaction --no-root

COPY . .

ENTRYPOINT ["poetry", "run", "python", "main.py"]