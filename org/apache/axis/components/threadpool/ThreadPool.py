DEFAULT_MAX_THREADS = "int  100"
def ThreadPool():
    '''    public ThreadPool()
    public ThreadPool(final int maxPoolSize)
    '''
def cleanup():
    '''    public void cleanup()
    '''
def isShutdown():
    '''    public boolean isShutdown()
    '''
def isShuttingDown():
    '''    public boolean isShuttingDown()
    '''
def getWorkerCount():
    '''    public long getWorkerCount()
    '''
def addWorker():
    '''    public void addWorker(final Runnable worker)
    '''
def interruptAll():
    '''    public void interruptAll()
    '''
def shutdown():
    '''    public void shutdown()
    '''
def safeShutdown():
    '''    public void safeShutdown()
    '''
def awaitShutdown():
    '''    public synchronized void awaitShutdown()
    public synchronized boolean awaitShutdown(final long timeout)
    '''
def workerDone():
    '''    public void workerDone(final Runnable worker, final boolean restart)
    '''
