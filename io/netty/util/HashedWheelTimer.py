WORKER_STATE_INIT = "int  0"
WORKER_STATE_STARTED = "int  1"
WORKER_STATE_SHUTDOWN = "int  2"
def HashedWheelTimer():
'''public HashedWheelTimer()
public HashedWheelTimer(final long tickDuration, final TimeUnit unit)
public HashedWheelTimer(final long tickDuration, final TimeUnit unit, final int ticksPerWheel)
public HashedWheelTimer(final ThreadFactory threadFactory)
public HashedWheelTimer(final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit)
public HashedWheelTimer(final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit, final int ticksPerWheel)
public HashedWheelTimer(final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit, final int ticksPerWheel, final boolean leakDetection)
public HashedWheelTimer(final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit, final int ticksPerWheel, final boolean leakDetection, final long maxPendingTimeouts)
'''
pass
def start():
'''public void start()
'''
pass
def stop():
'''public Set<Timeout> stop()
'''
pass
def newTimeout():
'''public Timeout newTimeout(final TimerTask task, final long delay, final TimeUnit unit)
'''
pass
def pendingTimeouts():
'''public long pendingTimeouts()
'''
pass
def run():
'''public void run()
'''
pass
def unprocessedTimeouts():
'''public Set<Timeout> unprocessedTimeouts()
'''
pass
def timer():
'''public Timer timer()
'''
pass
def task():
'''public TimerTask task()
'''
pass
def cancel():
'''public boolean cancel()
'''
pass
def compareAndSetState():
'''public boolean compareAndSetState(final int expected, final int state)
'''
pass
def state():
'''public int state()
'''
pass
def isCancelled():
'''public boolean isCancelled()
'''
pass
def isExpired():
'''public boolean isExpired()
'''
pass
def expire():
'''public void expire()
'''
pass
def toString():
'''public String toString()
'''
pass
def addTimeout():
'''public void addTimeout(final HashedWheelTimeout timeout)
'''
pass
def expireTimeouts():
'''public void expireTimeouts(final long deadline)
'''
pass
def remove():
'''public HashedWheelTimeout remove(final HashedWheelTimeout timeout)
'''
pass
def clearTimeouts():
'''public void clearTimeouts(final Set<Timeout> set)
'''
pass
