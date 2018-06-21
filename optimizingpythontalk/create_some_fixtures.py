import json
import random
from collections import defaultdict

names = ("alice", "bob", "charles", "dan", "eve")
repo_names = ("repo_a", "repo_b")

fixture_info = []
def _create_repos(repos):
    for idx, repo_name in enumerate(repos):
        fixture_info.append({
            "model" : "stats.repository",
            "pk" : idx,
            "fields" : {
                "repo_name"  : repo_name,
                "repo_url" : "https://example.com/"+repo_name,
            }
        })
_create_repos(repo_names)


def _create_commitcounts():

    commit_counts = list(range(1000))
    commit_info = defaultdict(list)

    for idx, commit_count in enumerate(commit_counts):
        current_name = random.choice(names)
        current_repo = random.choice([0,1])
        commit_info[current_name].append(commit_count)
        fixture_info.append({
            "model" : "stats.commitcounts",
            "pk" : idx,
            "fields" : {
                "repo"  : current_repo,
                "author_name" : current_name,
                "commit_count": commit_count,
            },
        })
    
_create_commitcounts()

with open("fixtures.json", "w") as fixtures_file:
    fixtures_file.write(json.dumps(fixture_info))
