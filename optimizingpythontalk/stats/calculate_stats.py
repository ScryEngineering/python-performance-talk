import statistics

from .models import Repository, CommitCounts

from silk.profiling.profiler import silk_profile

@silk_profile(name='faster average')
def faster_average(items):
    """Compute the mean (average) for an iterable"""
    return sum(items) / len(items)

@silk_profile(name='Standard library average')
def std_lib_average(items):
    return statistics.mean(items)