STOPPED = "String  \"STOPPED\""
FAILED = "String  \"FAILED\""
STARTING = "String  \"STARTING\""
STARTED = "String  \"STARTED\""
STOPPING = "String  \"STOPPING\""
RUNNING = "String  \"RUNNING\""
def ():
    '''returns AbstractLifeCycle\n\n
    ()\n
    '''
def isRunning():
    '''returns boolean\n\n
    isRunning()\n
    '''
def isStarted():
    '''returns boolean\n\n
    isStarted()\n
    '''
def isStarting():
    '''returns boolean\n\n
    isStarting()\n
    '''
def isStopping():
    '''returns boolean\n\n
    isStopping()\n
    '''
def isStopped():
    '''returns boolean\n\n
    isStopped()\n
    '''
def isFailed():
    '''returns boolean\n\n
    isFailed()\n
    '''
def addLifeCycleListener():
    '''returns None\n\n
    addLifeCycleListener(final Listener listener)\n
    '''
def removeLifeCycleListener():
    '''returns None\n\n
    removeLifeCycleListener(final Listener listener)\n
    '''
def getState():
    '''returns String\n\n
    getState()\n
    '''
def lifeCycleFailure():
    '''returns None\n\n
    lifeCycleFailure(final LifeCycle event, final Throwable cause)\n
    '''
def lifeCycleStarted():
    '''returns None\n\n
    lifeCycleStarted(final LifeCycle event)\n
    '''
def lifeCycleStarting():
    '''returns None\n\n
    lifeCycleStarting(final LifeCycle event)\n
    '''
def lifeCycleStopped():
    '''returns None\n\n
    lifeCycleStopped(final LifeCycle event)\n
    '''
def lifeCycleStopping():
    '''returns None\n\n
    lifeCycleStopping(final LifeCycle event)\n
    '''
