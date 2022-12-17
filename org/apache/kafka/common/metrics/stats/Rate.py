def ():
    '''returns SampledTotal\n\n
    ()\n
    (final TimeUnit unit)\n
    (final SampledStat stat)\n
    (final TimeUnit unit, final SampledStat stat)\n
    ()\n
    '''
def unitName():
    '''returns String\n\n
    unitName()\n
    '''
def record():
    '''returns None\n\n
    record(final MetricConfig config, final double value, final long timeMs)\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    '''
def windowSize():
    '''returns long\n\n
    windowSize(final MetricConfig config, final long now)\n
    '''
def combine():
    '''returns double\n\n
    combine(final List<Sample> samples, final MetricConfig config, final long now)\n
    '''
