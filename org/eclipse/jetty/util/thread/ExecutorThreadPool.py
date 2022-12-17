def ():
    '''returns ExecutorThreadPool\n\n
    (final ExecutorService executor)\n
    ()\n
    (final int queueSize)\n
    (final int corePoolSize, final int maximumPoolSize, final long keepAliveTime)\n
    (final int corePoolSize, final int maximumPoolSize, final long keepAliveTime, final TimeUnit unit)\n
    (final int corePoolSize, final int maximumPoolSize, final long keepAliveTime, final TimeUnit unit, final BlockingQueue<Runnable> workQueue)\n
    '''
def dispatch():
    '''returns boolean\n\n
    dispatch(final Runnable job)\n
    '''
def getIdleThreads():
    '''returns int\n\n
    getIdleThreads()\n
    '''
def getThreads():
    '''returns int\n\n
    getThreads()\n
    '''
def isLowOnThreads():
    '''returns boolean\n\n
    isLowOnThreads()\n
    '''
def join():
    '''returns None\n\n
    join()\n
    '''
