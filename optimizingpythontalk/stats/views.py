import statistics

from django.shortcuts import render
from django.http import HttpResponse

from .calculate_stats import faster_average, averages_with_threshold_fast
from .calculate_stats_slow import recursive_average, averages_with_threshold

from silk.profiling.profiler import silk_profile

import pprint


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

    items = range(10000)
    with silk_profile(name='faster average (%d items)' % len(items)):
        faster_average(items)
    with silk_profile(name='standard library average (%d items)' % len(items)):
        statistics.mean(items)
    return HttpResponse('Averages now calculated, to see how long it took go to <a href="/silk">/silk</a> url')


@silk_profile(name="Slow averages with threshold")
def averages_with_threshold_slow(request):
    threshold_number = 10
    results = averages_with_threshold(threshold_number)
    return HttpResponse('SLOW Averages with threshold of' + str(threshold_number) + 'commits \n ' + pprint.pformat(results) +' \n to see how long it took go to <a href="/silk">/silk</a> url')

@silk_profile(name="fast averages with threshold")
def averages_with_threshold_faster(request):
    threshold_number = 10
    results = averages_with_threshold_fast(threshold_number)
    return HttpResponse('FAST Averages with threshold of' + str(threshold_number) + 'commits \n ' + pprint.pformat(results) +'\n to see how long it took go to <a href="/silk">/silk</a> url')
