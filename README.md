# Adkom Backend

Modular Django + DRF backend with reusable app architecture.

## Apps

- core (base models & utilities)
- notification
- product
- accounts
- cart
- checkout
- blog

## Architecture

- selectors.py → read/query logic
- services.py → business logic
- serializers.py → DRF layer
- views.py → request/response
- models/ → database
- signals.py → events
- notifications.py → message builders

## Setup

```bash
python -m venv venv
venv\Scripts\activate  # windows

pip install -r requirements-dev.txt

python manage.py migrate
python manage.py runserver