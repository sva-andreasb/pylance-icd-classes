WORKER_STATE_INIT = "int  0"
WORKER_STATE_STARTED = "int  1"
WORKER_STATE_SHUTDOWN = "int  2"
def HashedWheelTimer():
    '''    public HashedWheelTimer()
    public HashedWheelTimer(final long tickDuration, final TimeUnit unit)
    public HashedWheelTimer(final long tickDuration, final TimeUnit unit, final int ticksPerWheel)
    public HashedWheelTimer(final ThreadFactory threadFactory)
    public HashedWheelTimer(final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit)
    public HashedWheelTimer(final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit, final int ticksPerWheel)
    public HashedWheelTimer(final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit, final int ticksPerWheel, final boolean leakDetection)
    public HashedWheelTimer(final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit, final int ticksPerWheel, final boolean leakDetection, final long maxPendingTimeouts)
    '''
def start():
    '''    public void start()
    '''
def stop():
    '''    public Set<Timeout> stop()
    '''
def newTimeout():
    '''    public Timeout newTimeout(final TimerTask task, final long delay, final TimeUnit unit)
    '''
def pendingTimeouts():
    '''    public long pendingTimeouts()
    '''
def run():
    '''    public void run()
    '''
def unprocessedTimeouts():
    '''    public Set<Timeout> unprocessedTimeouts()
    '''
def timer():
    '''    public Timer timer()
    '''
def task():
    '''    public TimerTask task()
    '''
def cancel():
    '''    public boolean cancel()
    '''
def compareAndSetState():
    '''    public boolean compareAndSetState(final int expected, final int state)
    '''
def state():
    '''    public int state()
    '''
def isCancelled():
    '''    public boolean isCancelled()
    '''
def isExpired():
    '''    public boolean isExpired()
    '''
def expire():
    '''    public void expire()
    '''
def toString():
    '''    public String toString()
    '''
def addTimeout():
    '''    public void addTimeout(final HashedWheelTimeout timeout)
    '''
def expireTimeouts():
    '''    public void expireTimeouts(final long deadline)
    '''
def remove():
    '''    public HashedWheelTimeout remove(final HashedWheelTimeout timeout)
    '''
def clearTimeouts():
    '''    public void clearTimeouts(final Set<Timeout> set)
    '''
