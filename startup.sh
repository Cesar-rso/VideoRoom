gunicorn --bind=0.0.0.0:8000 --workers=2 VideoRoom.wsgi --daemon
nginx -g 'daemon off;'