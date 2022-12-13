NO_LIMIT = "int  0"
def TimedSemaphore():
    '''    public TimedSemaphore(final long timePeriod, final TimeUnit timeUnit, final int limit)
    public TimedSemaphore(final ScheduledExecutorService service, final long timePeriod, final TimeUnit timeUnit, final int limit)
    '''
def getLimit():
    '''    public final synchronized int getLimit()
    '''
def setLimit():
    '''    public final synchronized void setLimit(final int limit)
    '''
def shutdown():
    '''    public synchronized void shutdown()
    '''
def isShutdown():
    '''    public synchronized boolean isShutdown()
    '''
def acquire():
    '''    public synchronized void acquire()
    '''
def getLastAcquiresPerPeriod():
    '''    public synchronized int getLastAcquiresPerPeriod()
    '''
def getAcquireCount():
    '''    public synchronized int getAcquireCount()
    '''
def getAvailablePermits():
    '''    public synchronized int getAvailablePermits()
    '''
def getAverageCallsPerPeriod():
    '''    public synchronized double getAverageCallsPerPeriod()
    '''
def getPeriod():
    '''    public long getPeriod()
    '''
def getUnit():
    '''    public TimeUnit getUnit()
    '''
def run():
    '''    public void run()
    '''
