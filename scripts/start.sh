sed -i "s/DEBUG = True/DEBUG = False/g" /opt/project/squirro/squirro/settings.py
sed -i "s/ALLOWED_HOSTS = []/ALLOWED_HOSTS = ['*']/g" /opt/project/squirro/squirro/settings.py
cd /opt/project/squirro/
python3 /opt/project/squirro/manage.py migrate
gunicorn --chdir squirro --bind 0.0.0.0:8000 squirro.wsgi:application