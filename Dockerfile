
FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY shop/ .

# for run on VPS + nginx:
CMD ["gunicorn", "shop.wsgi:application", "--bind", "0:8000" ]

# for run on localhost:
# CMD ["python3", "manage.py", "runserver", "0:8000"]
