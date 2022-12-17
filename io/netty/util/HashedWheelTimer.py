WORKER_STATE_INIT = "int  0"
WORKER_STATE_STARTED = "int  1"
WORKER_STATE_SHUTDOWN = "int  2"
def ():
    '''returns HashedWheelTimer\n\n
    ()\n
    (final long tickDuration, final TimeUnit unit)\n
    (final long tickDuration, final TimeUnit unit, final int ticksPerWheel)\n
    (final ThreadFactory threadFactory)\n
    (final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit)\n
    (final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit, final int ticksPerWheel)\n
    (final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit, final int ticksPerWheel, final boolean leakDetection)\n
    (final ThreadFactory threadFactory, final long tickDuration, final TimeUnit unit, final int ticksPerWheel, final boolean leakDetection, final long maxPendingTimeouts)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns Set<Timeout>\n\n
    stop()\n
    '''
def newTimeout():
    '''returns Timeout\n\n
    newTimeout(final TimerTask task, final long delay, final TimeUnit unit)\n
    '''
def pendingTimeouts():
    '''returns long\n\n
    pendingTimeouts()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def unprocessedTimeouts():
    '''returns Set<Timeout>\n\n
    unprocessedTimeouts()\n
    '''
def timer():
    '''returns Timer\n\n
    timer()\n
    '''
def task():
    '''returns TimerTask\n\n
    task()\n
    '''
def cancel():
    '''returns boolean\n\n
    cancel()\n
    '''
def compareAndSetState():
    '''returns boolean\n\n
    compareAndSetState(final int expected, final int state)\n
    '''
def state():
    '''returns int\n\n
    state()\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    '''
def isExpired():
    '''returns boolean\n\n
    isExpired()\n
    '''
def expire():
    '''returns None\n\n
    expire()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def addTimeout():
    '''returns None\n\n
    addTimeout(final HashedWheelTimeout timeout)\n
    '''
def expireTimeouts():
    '''returns None\n\n
    expireTimeouts(final long deadline)\n
    '''
def remove():
    '''returns HashedWheelTimeout\n\n
    remove(final HashedWheelTimeout timeout)\n
    '''
def clearTimeouts():
    '''returns None\n\n
    clearTimeouts(final Set<Timeout> set)\n
    '''
