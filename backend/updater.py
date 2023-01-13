from apscheduler.schedulers.background import BackgroundScheduler
import dataupdater


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(dataupdater.get_current_conditions, 'cron', minute='*/15')
    scheduler.add_job(dataupdater.get_forecast, 'cron', hour='01', minute='00')
    scheduler.start()
