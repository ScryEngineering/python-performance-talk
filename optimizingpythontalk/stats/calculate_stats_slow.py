from .models import Repository, CommitCounts

def recursive_average(items, cumulative_sum=0, count=0):
    """Compute the mean (average) for an iterable"""
    if not items:
        return cumulative_sum / count
    else:
        return recursive_average(items[1:], cumulative_sum+items[0], count+1)


