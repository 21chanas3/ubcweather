# Running the App
- In `/frontend`, run `npm run dev`
- In root dir, run `python manage.py runserver`

# Scheduling CRON jobs
- Use `crontab -e`
- `*/15 * * * * /path/to/venv /path/to/manage.py getcondition`
- `0 3 * * * /path/to/venv /path/to/manage.py getforecast`
