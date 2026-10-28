# Deployment checklist (Azure App Service)

1. Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=false`, `DJANGO_ALLOWED_HOSTS`, `DB_ENGINE=mysql`, and `MYSQL_*` values in App Service configuration.
2. Use Azure Database for MySQL with TLS and a private network where available; never commit production secrets.
3. Run migrations as a controlled release step and create an application administrator separately.
4. Build the React app with `npm run build`; host the static output or serve it from a configured static host, and set `VITE_API_URL` to the public API base.
5. Configure CORS to the exact frontend origin, HTTPS, health probes, logs, backups, and deployment slots.
6. Tests and example records are not evidence of the résumé's stated traffic, response times, or team size; measure those independently before claiming them.
