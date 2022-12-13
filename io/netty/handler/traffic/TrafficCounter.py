def milliSecondFromNano():
'''public static long milliSecondFromNano()
'''
pass
def start():
'''public synchronized void start()
'''
pass
def stop():
'''public synchronized void stop()
'''
pass
def TrafficCounter():
'''public TrafficCounter(final ScheduledExecutorService executor, final String name, final long checkInterval)
public TrafficCounter(final AbstractTrafficShapingHandler trafficShapingHandler, final ScheduledExecutorService executor, final String name, final long checkInterval)
'''
pass
def configure():
'''public void configure(final long newCheckInterval)
'''
pass
def checkInterval():
'''public long checkInterval()
'''
pass
def lastReadThroughput():
'''public long lastReadThroughput()
'''
pass
def lastWriteThroughput():
'''public long lastWriteThroughput()
'''
pass
def lastReadBytes():
'''public long lastReadBytes()
'''
pass
def lastWrittenBytes():
'''public long lastWrittenBytes()
'''
pass
def currentReadBytes():
'''public long currentReadBytes()
'''
pass
def currentWrittenBytes():
'''public long currentWrittenBytes()
'''
pass
def lastTime():
'''public long lastTime()
'''
pass
def cumulativeWrittenBytes():
'''public long cumulativeWrittenBytes()
'''
pass
def cumulativeReadBytes():
'''public long cumulativeReadBytes()
'''
pass
def lastCumulativeTime():
'''public long lastCumulativeTime()
'''
pass
def getRealWrittenBytes():
'''public AtomicLong getRealWrittenBytes()
'''
pass
def getRealWriteThroughput():
'''public long getRealWriteThroughput()
'''
pass
def resetCumulativeTime():
'''public void resetCumulativeTime()
'''
pass
def name():
'''public String name()
'''
pass
def readTimeToWait():
'''public long readTimeToWait(final long size, final long limitTraffic, final long maxTime)
public long readTimeToWait(final long size, final long limitTraffic, final long maxTime, final long now)
'''
pass
def writeTimeToWait():
'''public long writeTimeToWait(final long size, final long limitTraffic, final long maxTime)
public long writeTimeToWait(final long size, final long limitTraffic, final long maxTime, final long now)
'''
pass
def toString():
'''public String toString()
'''
pass
def run():
'''public void run()
'''
pass
