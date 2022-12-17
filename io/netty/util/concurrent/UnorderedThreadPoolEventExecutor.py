def ():
    '''returns UnorderedThreadPoolEventExecutor\n\n
    (final int corePoolSize)\n
    (final int corePoolSize, final ThreadFactory threadFactory)\n
    (final int corePoolSize, final RejectedExecutionHandler handler)\n
    (final int corePoolSize, final ThreadFactory threadFactory, final RejectedExecutionHandler handler)\n
    '''
def next():
    '''returns EventExecutor\n\n
    next()\n
    '''
def parent():
    '''returns EventExecutorGroup\n\n
    parent()\n
    '''
def inEventLoop():
    '''returns boolean\n\n
    inEventLoop()\n
    inEventLoop(final Thread thread)\n
    '''
def isShuttingDown():
    '''returns boolean\n\n
    isShuttingDown()\n
    '''
def shutdownNow():
    '''returns List<Runnable>\n\n
    shutdownNow()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def iterator():
    '''returns Iterator<EventExecutor>\n\n
    iterator()\n
    '''
def execute():
    '''returns None\n\n
    execute(final Runnable command)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def isPeriodic():
    '''returns boolean\n\n
    isPeriodic()\n
    '''
def getDelay():
    '''returns long\n\n
    getDelay(final TimeUnit unit)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Delayed o)\n
    '''
