from django.db import models

class Repository(models.Model):
    """Represent a repository"""
    repo_url = models.CharField(max_length=30)
    repo_name = models.CharField(max_length=30)

    def __str__(self):
        return self.repo_name

class CommitCounts(models.Model):
    """Respresent commit counts by author for a repo"""
    author_name = models.CharField(max_length=30)
    commit_count = models.IntegerField()
    repo = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
        verbose_name="the related repository",
    )

    def __str__(self):
        return "{} - {} commits".format(self.author_name, self.commit_count)