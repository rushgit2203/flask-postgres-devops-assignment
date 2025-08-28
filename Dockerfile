# Stage 1: Builder
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY app/ ./app
EXPOSE 8000
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
USER 1000
CMD ["python", "app/app.py"]

