FROM python:3
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY menu_app .
CMD ["gunicorn", "menu_app.wsgi:application", "--bind", "0:8000" ]