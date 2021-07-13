release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py loaddata products.json --no-input

web: gunicorn techdailyapi.wsgi
