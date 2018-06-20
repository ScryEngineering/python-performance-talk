from .models import Repository, CommitCounts

from silk.profiling.profiler import silk_profile

def recursive_average(items, cumulative_sum=0, count=0):
    """Compute the mean (average) for an iterable"""
    if not items:
        return cumulative_sum / count
    return recursive_average(items[1:], cumulative_sum+items[0], count+1)

authors_plus_commit_info = []
authors = {}
def averages_with_threshold(threshold: int) -> dict:
    """Threshold is the minimum number of commits for inclusion"""
    authors_plus_commit_info.clear()
    authors.clear()
    for commit_info in CommitCounts.objects.all():
        if commit_info.commit_count > threshold:
            authors_plus_commit_info.append(
                (commit_info.author_name, commit_info.commit_count)
            )
    for item in authors_plus_commit_info:
        try:
            authors[item[0]]
        except KeyError:
            authors[item[0]] = [item[1]]
        else:
            authors[item[0]].append(item[1])
    return {author: recursive_average(items) for author, items in authors.items()}
