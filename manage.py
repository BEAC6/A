#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Add the project root directory to the Python path to ensure module resolution.
    # This is the most robust way to solve ModuleNotFoundError on platforms like Render.
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alhassan.production_settings')
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
