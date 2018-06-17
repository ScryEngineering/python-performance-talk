from django.test import TestCase

from .models import Repository, CommitCounts

class StatsTestCase(TestCase):
    def setUp(self):
        a = Repository.objects.create(repo_url="a.example.com", repo_name="a")
        b = Repository.objects.create(repo_url="b.example.com", repo_name="b")

        CommitCounts.objects.create(author_name="bob", repo=a, commit_count=10)
        CommitCounts.objects.create(author_name="bob", repo=b, commit_count=2)
        CommitCounts.objects.create(author_name="alice", repo=a, commit_count=20)
        CommitCounts.objects.create(author_name="alice", repo=b, commit_count=20)
        CommitCounts.objects.create(author_name="eve", repo=b, commit_count=10)

    def test_recursive_averages(self):
        """Test the recursive average function"""
        from statistics import mean
        from .calculate_stats_slow import recursive_average
        a = [1,2,3,4,5]
        b = [0.1, 3, 2.0, 0.45]
        assert recursive_average(a) == mean(a)
        assert recursive_average(b) == mean(b)

    def test_pure_averages(self):
        """test that a threshold of zero gives the average"""
        from .calculate_stats_slow import averages_with_threshold
        results = averages_with_threshold(0)
        assert len(results) == 3 # No authors filtered out
        assert results["bob"] == (10 + 2) / 2
        assert results["alice"] == (20 + 20) / 2
        assert results["eve"] == 10
