import simplecomputingcluster as scc
from simplecomputingcluster.jobs import install, uninstall

# this should be registered as a worker queue.
install("aa2atom")
# uninstall("aa2atom")


functions_to_register = [
    "simplecomputingcluster.jobs.long_lasting_job_simulation",
    "aa2atom.aa2atom.aa2atom"
]
FLASK_URL = "http://192.168.178.20:8957"

scc.register.register_as_jobs(functions_to_register, FLASK_URL)
scc.register.register_post_call(
    functions_to_register,
    FLASK_URL
)
scc.register.register_post_queue(
    functions_to_register,
    FLASK_URL
)

from simplecomputingcluster.jobs import long_lasting_job_simulation


long_lasting_job_simulation
long_lasting_job_simulation(.1)
long_lasting_job_simulation.post_call(seconds=.1)
long_lasting_job_simulation.post_queue(.1)


from aa2atom.aa2atom import aa2atom

aa2atom("AAASEQ")
aa2atom.post_call("AAASEQ")
aa2atom.post_queue("AAASEQ")
