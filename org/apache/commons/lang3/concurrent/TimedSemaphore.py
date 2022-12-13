NO_LIMIT = "int  0"
def TimedSemaphore():
'''public TimedSemaphore(final long timePeriod, final TimeUnit timeUnit, final int limit)
public TimedSemaphore(final ScheduledExecutorService service, final long timePeriod, final TimeUnit timeUnit, final int limit)
'''
pass
def getLimit():
'''public final synchronized int getLimit()
'''
pass
def setLimit():
'''public final synchronized void setLimit(final int limit)
'''
pass
def shutdown():
'''public synchronized void shutdown()
'''
pass
def isShutdown():
'''public synchronized boolean isShutdown()
'''
pass
def acquire():
'''public synchronized void acquire()
'''
pass
def getLastAcquiresPerPeriod():
'''public synchronized int getLastAcquiresPerPeriod()
'''
pass
def getAcquireCount():
'''public synchronized int getAcquireCount()
'''
pass
def getAvailablePermits():
'''public synchronized int getAvailablePermits()
'''
pass
def getAverageCallsPerPeriod():
'''public synchronized double getAverageCallsPerPeriod()
'''
pass
def getPeriod():
'''public long getPeriod()
'''
pass
def getUnit():
'''public TimeUnit getUnit()
'''
pass
def run():
'''public void run()
'''
pass
