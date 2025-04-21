# manage.py
import os
import sys  # Add this line to import sys
import django
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

django.setup()

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
