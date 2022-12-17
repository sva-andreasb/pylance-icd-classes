def ():
    '''returns Frequencies\n\n
    (final int buckets, final double min, final double max, final Frequency... frequencies)\n
    '''
def stats():
    '''returns List<NamedMeasurable>\n\n
    stats()\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    '''
def frequency():
    '''returns double\n\n
    frequency(final MetricConfig config, final long now, final double centerValue)\n
    '''
def combine():
    '''returns double\n\n
    combine(final List<Sample> samples, final MetricConfig config, final long now)\n
    '''
def reset():
    '''returns None\n\n
    reset(final long now)\n
    '''
