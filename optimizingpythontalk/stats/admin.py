from django.contrib import admin
from .models import Repository, CommitCounts

admin.register(Repository)
admin.register(CommitCounts)