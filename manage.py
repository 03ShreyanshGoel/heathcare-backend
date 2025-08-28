#!/usr/bin/env python
import os
import sys

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU2Mzc1MDgyLCJpYXQiOjE3NTYzNzQ3ODIsImp0aSI6IjdmYjZjZWQwMGNlZjQ4Njg5ZGQwM2MxODBkZTBmNDg0IiwidXNlcl9pZCI6IjIifQ.ZCRQfO_dXidD49PQ5eica80ricMg-55gKzidRB31dnY

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()