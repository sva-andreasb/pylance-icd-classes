def ():
    '''returns Percentiles\n\n
    (final int sizeInBytes, final double max, final BucketSizing bucketing, final Percentile... percentiles)\n
    (final int sizeInBytes, final double min, final double max, final BucketSizing bucketing, final Percentile... percentiles)\n
    '''
def stats():
    '''returns List<NamedMeasurable>\n\n
    stats()\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    '''
def value():
    '''returns double\n\n
    value(final MetricConfig config, final long now, final double quantile)\n
    '''
def combine():
    '''returns double\n\n
    combine(final List<Sample> samples, final MetricConfig config, final long now)\n
    '''
def reset():
    '''returns None\n\n
    reset(final long now)\n
    '''
