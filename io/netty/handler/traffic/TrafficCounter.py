def milliSecondFromNano():
    '''public static long milliSecondFromNano()
    '''
def start():
    '''public synchronized void start()
    '''
def stop():
    '''public synchronized void stop()
    '''
def TrafficCounter():
    '''public TrafficCounter(final ScheduledExecutorService executor, final String name, final long checkInterval)
    public TrafficCounter(final AbstractTrafficShapingHandler trafficShapingHandler, final ScheduledExecutorService executor, final String name, final long checkInterval)
    '''
def configure():
    '''public void configure(final long newCheckInterval)
    '''
def checkInterval():
    '''public long checkInterval()
    '''
def lastReadThroughput():
    '''public long lastReadThroughput()
    '''
def lastWriteThroughput():
    '''public long lastWriteThroughput()
    '''
def lastReadBytes():
    '''public long lastReadBytes()
    '''
def lastWrittenBytes():
    '''public long lastWrittenBytes()
    '''
def currentReadBytes():
    '''public long currentReadBytes()
    '''
def currentWrittenBytes():
    '''public long currentWrittenBytes()
    '''
def lastTime():
    '''public long lastTime()
    '''
def cumulativeWrittenBytes():
    '''public long cumulativeWrittenBytes()
    '''
def cumulativeReadBytes():
    '''public long cumulativeReadBytes()
    '''
def lastCumulativeTime():
    '''public long lastCumulativeTime()
    '''
def getRealWrittenBytes():
    '''public AtomicLong getRealWrittenBytes()
    '''
def getRealWriteThroughput():
    '''public long getRealWriteThroughput()
    '''
def resetCumulativeTime():
    '''public void resetCumulativeTime()
    '''
def name():
    '''public String name()
    '''
def readTimeToWait():
    '''public long readTimeToWait(final long size, final long limitTraffic, final long maxTime)
    public long readTimeToWait(final long size, final long limitTraffic, final long maxTime, final long now)
    '''
def writeTimeToWait():
    '''public long writeTimeToWait(final long size, final long limitTraffic, final long maxTime)
    public long writeTimeToWait(final long size, final long limitTraffic, final long maxTime, final long now)
    '''
def toString():
    '''public String toString()
    '''
def run():
    '''public void run()
    '''
