from artiq.experiment import *
# should fail
import foo


class OutOfRepoExp(EnvExperiment):
    pass
