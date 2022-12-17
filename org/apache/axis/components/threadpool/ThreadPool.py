DEFAULT_MAX_THREADS = "int  100"
def ():
    '''returns ThreadPool\n\n
    ()\n
    (final int maxPoolSize)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def isShutdown():
    '''returns boolean\n\n
    isShutdown()\n
    '''
def isShuttingDown():
    '''returns boolean\n\n
    isShuttingDown()\n
    '''
def getWorkerCount():
    '''returns long\n\n
    getWorkerCount()\n
    '''
def addWorker():
    '''returns None\n\n
    addWorker(final Runnable worker)\n
    '''
def interruptAll():
    '''returns None\n\n
    interruptAll()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def safeShutdown():
    '''returns None\n\n
    safeShutdown()\n
    '''
def workerDone():
    '''returns None\n\n
    workerDone(final Runnable worker, final boolean restart)\n
    '''
