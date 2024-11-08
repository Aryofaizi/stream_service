from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from core.v2.views import fetch_tmdb_data, populate_content_table


def start():
    scheduler = BackgroundScheduler()
    # Set the job to run at 11:47 PM every day
    trigger = CronTrigger(hour=23, minute=47)
    scheduler.add_job(fetch_tmdb_data, trigger=trigger)  # Pass the function reference, not its result
    # extract movies data from tmdb
    scheduler.add_job(populate_content_table, trigger=trigger)
    scheduler.start()



