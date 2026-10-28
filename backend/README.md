# Django API

- `python manage.py migrate` creates tables.
- `python manage.py seed_demo` inserts a sample student, recruiter, and opportunity.
- `pytest` runs API tests.
- API resources are paginated at 20 rows per page; student and opportunity search use `?search=`.
- For MySQL, install a compiler and MySQL development headers if `mysqlclient` needs to be built from source.
