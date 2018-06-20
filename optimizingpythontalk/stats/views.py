import statistics

from django.shortcuts import render
from django.http import HttpResponse

from .calculate_stats import faster_average
from .calculate_stats_slow import recursive_average

from silk.profiling.profiler import silk_profile

import sys
sys.setrecursionlimit(1005)

def calculate_averages(request):
    """Kick off the various functions that will the average stats given a threshold"""
    items = range(100)
    with silk_profile(name='Recursive average (%d items)' % len(items)):
        recursive_average(items)
    with silk_profile(name='faster average (%d items)' % len(items)):
        faster_average(items)
    with silk_profile(name='standard library average (%d items)' % len(items)):
        statistics.mean(items)

    items = range(900)
    with silk_profile(name='Recursive average (%d items)' % len(items)):
        recursive_average(items)
    with silk_profile(name='faster average (%d items)' % len(items)):
        faster_average(items)
    with silk_profile(name='standard library average (%d items)' % len(items)):
        statistics.mean(items)
    return HttpResponse("Averages now calculated, to see how long it took go to /silk url")