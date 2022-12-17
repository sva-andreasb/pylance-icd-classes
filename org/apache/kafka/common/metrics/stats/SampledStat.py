def ():
    '''returns Sample\n\n
    (final double initialValue)\n
    (final double initialValue, final long now)\n
    '''
def record():
    '''returns None\n\n
    record(final MetricConfig config, final double value, final long timeMs)\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    '''
def current():
    '''returns Sample\n\n
    current(final long timeMs)\n
    '''
def oldest():
    '''returns Sample\n\n
    oldest(final long now)\n
    '''
def reset():
    '''returns None\n\n
    reset(final long now)\n
    '''
def isComplete():
    '''returns boolean\n\n
    isComplete(final long timeMs, final MetricConfig config)\n
    '''
