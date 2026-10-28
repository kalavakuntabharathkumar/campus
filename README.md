# CampusConnect — Placement & Internship Portal

A starter full-stack portal for students, recruiters, and placement officers. Django REST Framework serves the API; React provides a lightweight dashboard; MySQL is the configured database.

## Run the API
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate | macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
API base: `http://127.0.0.1:8000/api/`; admin: `/admin/`.

## Run the frontend
```bash
cd frontend
npm install
npm run dev
```
Set `VITE_API_URL` to the API base URL if it is not `http://127.0.0.1:8000/api`.

For a quick local start, the backend defaults to SQLite when `DB_ENGINE=sqlite`; set `DB_ENGINE=mysql` and the `MYSQL_*` variables for MySQL. Do not use debug mode or development secrets in production.
