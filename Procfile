release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py loaddata fixture products.json

web: gunicorn techdailyapi.wsgi
