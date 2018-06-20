import statistics

from .models import Repository, CommitCounts

def faster_average(items):
    """Compute the mean (average) for an iterable"""
    return sum(items) / len(items)

def std_lib_average(items):
    return statistics.mean(items)