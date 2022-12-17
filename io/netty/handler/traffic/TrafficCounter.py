def ():
    '''returns TrafficCounter\n\n
    (final ScheduledExecutorService executor, final String name, final long checkInterval)\n
    (final AbstractTrafficShapingHandler trafficShapingHandler, final ScheduledExecutorService executor, final String name, final long checkInterval)\n
    '''
def configure():
    '''returns None\n\n
    configure(final long newCheckInterval)\n
    '''
def checkInterval():
    '''returns long\n\n
    checkInterval()\n
    '''
def lastReadThroughput():
    '''returns long\n\n
    lastReadThroughput()\n
    '''
def lastWriteThroughput():
    '''returns long\n\n
    lastWriteThroughput()\n
    '''
def lastReadBytes():
    '''returns long\n\n
    lastReadBytes()\n
    '''
def lastWrittenBytes():
    '''returns long\n\n
    lastWrittenBytes()\n
    '''
def currentReadBytes():
    '''returns long\n\n
    currentReadBytes()\n
    '''
def currentWrittenBytes():
    '''returns long\n\n
    currentWrittenBytes()\n
    '''
def lastTime():
    '''returns long\n\n
    lastTime()\n
    '''
def cumulativeWrittenBytes():
    '''returns long\n\n
    cumulativeWrittenBytes()\n
    '''
def cumulativeReadBytes():
    '''returns long\n\n
    cumulativeReadBytes()\n
    '''
def lastCumulativeTime():
    '''returns long\n\n
    lastCumulativeTime()\n
    '''
def getRealWrittenBytes():
    '''returns AtomicLong\n\n
    getRealWrittenBytes()\n
    '''
def getRealWriteThroughput():
    '''returns long\n\n
    getRealWriteThroughput()\n
    '''
def resetCumulativeTime():
    '''returns None\n\n
    resetCumulativeTime()\n
    '''
def name():
    '''returns String\n\n
    name()\n
    '''
def readTimeToWait():
    '''returns long\n\n
    readTimeToWait(final long size, final long limitTraffic, final long maxTime)\n
    readTimeToWait(final long size, final long limitTraffic, final long maxTime, final long now)\n
    '''
def writeTimeToWait():
    '''returns long\n\n
    writeTimeToWait(final long size, final long limitTraffic, final long maxTime)\n
    writeTimeToWait(final long size, final long limitTraffic, final long maxTime, final long now)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
