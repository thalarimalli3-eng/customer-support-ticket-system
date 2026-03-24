
# Customer Support Ticket System (Django)

Simple helpdesk system with:
- Ticket creation
- Status tracking
- Admin dashboard

## Tech
- Python
- Django
- PostgreSQL (SQLite for local dev)

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
http://127.0.0.1:8000/

Admin:
http://127.0.0.1:8000/admin
