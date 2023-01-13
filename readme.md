# Running the App
- In `/frontend`, run `npm run dev`
- In root dir, run `python manage.py runserver`

# Scheduling CRON jobs
- Use `crontab -e`
- `*/15 * * * * /usr/bin/python3 /path/to/weatherupdater/conditionscript`
- `0 1 * * * /usr/bin/python3 /path/to/weatherupdater/forecastscript`