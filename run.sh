# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install Django
pip install Django

# Navigate to the project directory
cd architecturesite

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
