set -o errexit

python -m pip install --upgrade pip

pip install -r requirment.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
