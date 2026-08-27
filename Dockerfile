FROM python:3.14-slim

LABEL org.opencontainers.image.source="https://github.com/billalhossainjoy/django-movie-site"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN addgroup --system app && \
    adduser --system --ingroup app --home /home/app app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY --chown=app:app . .

RUN DJANGO_DEBUG=True python manage.py collectstatic --noinput && \
    mkdir -p /data && \
    chown app:app /data

ENV DJANGO_DEBUG=False \
    DJANGO_SECRET_KEY="f^&rb11ipony(k84!@y!+2hi@tww=l!ww&9fssuy-h)ngshgr+" \
    DJANGO_ALLOWED_HOSTS="django.billalhossain.dev,localhost,127.0.0.1,[::1]" \
    DJANGO_CSRF_TRUSTED_ORIGINS="https://django.billalhossain.dev" \
    DJANGO_TRUST_PROXY_HEADERS=True \
    SQLITE_PATH=/data/db.sqlite3

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD ["python", "-c", "import os, urllib.request; urllib.request.urlopen(f'http://127.0.0.1:{os.getenv(\"PORT\", \"8000\")}/', timeout=3)"]

CMD ["sh", "-c", "python manage.py migrate --noinput && exec gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000} --access-logfile - --error-logfile -"]
