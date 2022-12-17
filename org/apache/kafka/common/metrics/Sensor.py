def name():
    '''returns String\n\n
    name()\n
    '''
def record():
    '''returns None\n\n
    record()\n
    record(final double value)\n
    record(final double value, final long timeMs)\n
    record(final double value, final long timeMs, final boolean checkQuotas)\n
    '''
def shouldRecord():
    '''returns boolean\n\n
    shouldRecord()\n
    shouldRecord(final int configId)\n
    '''
def checkQuotas():
    '''returns None\n\n
    checkQuotas()\n
    checkQuotas(final long timeMs)\n
    '''
def add():
    '''returns None\n\n
    add(final CompoundStat stat)\n
    add(final MetricName metricName, final MeasurableStat stat)\n
    '''
def hasExpired():
    '''returns boolean\n\n
    hasExpired()\n
    '''
