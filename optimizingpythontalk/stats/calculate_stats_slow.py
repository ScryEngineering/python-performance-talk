from .models import Repository, CommitCounts

def recursive_average(items, cumulative_sum=0, count=0):
    """Compute the mean (average) for an iterable"""
    if not items:
        return cumulative_sum / count
    else:
        return recursive_average(items[1:], cumulative_sum+items[0], count+1)

def averages_with_threshold(threshold: int) -> dict:
    """Threshold is the minimum number of commits for inclusion"""
    authors_plus_commit_info = []
    for commit_info in CommitCounts.objects.all():
        if commit_info.commit_count > threshold:
            authors_plus_commit_info.append(
                (commit_info.author_name, commit_info.commit_count)
            )

    authors = {}
    for item in authors_plus_commit_info:
        try:
            authors[item[0]]
        except KeyError:
            authors[item[0]] = [item[1]]
        else:
            authors[item[0]].append(item[1])
    return {author: recursive_average(items) for author, items in authors.items()}
