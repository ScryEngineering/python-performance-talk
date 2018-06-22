import statistics
from collections import defaultdict

from .models import Repository, CommitCounts

def faster_average(items):
    """Compute the mean (average) for an iterable"""
    return sum(items) / len(items)

def std_lib_average(items):
    return statistics.mean(items)

def averages_with_threshold_fast(threshold: int) -> dict:
    """This attempts to be faster than the "slow" version of the code,
    But doesn't have especially good performance due to a not so great query"""
    commit_counts = defaultdict(list)
    for commit_info in CommitCounts.objects.filter(commit_count__gt=threshold):
        commit_counts[commit_info.author_name].append(commit_info.commit_count)
    return {author: faster_average(counts) for author, counts in commit_counts.items()}
