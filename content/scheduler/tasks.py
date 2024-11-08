from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from core.v2.views import fetch_tmdb_data


def start():
    scheduler = BackgroundScheduler()
    # Set the job to run at 11:47 PM every day
    trigger = CronTrigger(hour=23, minute=47)
    scheduler.add_job(fetch_tmdb_data, trigger=trigger)  # Pass the function reference, not its result
    scheduler.start()



