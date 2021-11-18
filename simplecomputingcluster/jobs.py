import rq.job
import time
import subprocess
import sys


def long_lasting_job_simulation(seconds):
    """Simulates long lasting job."""
    time.sleep(seconds)
    return f"Slept for {seconds} seconds."


def job_to_dict(job):
    """Translate a job instance to a dictionary."""
    return {
        k[1:] if k[0] == '_' else k:v
        for k, v in job.__dict__.items() if isinstance(v, (str,int,float))
    }


def get_job_status(job_id):
    """Get the status of a job."""
    try:
        job = rq.job.Job.fetch(job_id, connection=rq.connection)
        return get_job_details(job)
    except rq.job.NoSuchJobError:
        return {"result": "eliminated"}


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def uninstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package, "-y"])
