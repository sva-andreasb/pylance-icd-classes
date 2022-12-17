def ():
    '''returns Meter\n\n
    (final MetricName rateMetricName, final MetricName totalMetricName)\n
    (final TimeUnit unit, final MetricName rateMetricName, final MetricName totalMetricName)\n
    (final SampledStat rateStat, final MetricName rateMetricName, final MetricName totalMetricName)\n
    (final TimeUnit unit, final SampledStat rateStat, final MetricName rateMetricName, final MetricName totalMetricName)\n
    '''
def stats():
    '''returns List<NamedMeasurable>\n\n
    stats()\n
    '''
def record():
    '''returns None\n\n
    record(final MetricConfig config, final double value, final long timeMs)\n
    '''
