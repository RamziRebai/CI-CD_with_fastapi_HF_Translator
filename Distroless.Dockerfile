FROM python:3.7-slim-buster as build-env
COPY ./app /app
WORKDIR /app

FROM gcr.io/distroless/python3:fastapi1
COPY --from=build-env /app /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt && \
        rm requirements.txt
EXPOSE 80
CMD ["uvivorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]