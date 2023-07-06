# Install Dependencies
pip3 install -r deps.txt
# Run Migrations
python manage.py collectstatic --no-input
python3 manage.py migrate
