FROM python:3.12

WORKDIR /app

COPY ../../pyproject.toml ../../poetry.lock ./

RUN pip install poetry && poetry install --no-dev

COPY . .

EXPOSE 8080

CMD ["poetry", "run", "uvicorn", "lecture_2.hw.shop_api.main:app", "--host", "0.0.0.0", "--port", "8080"]
