STOPPED = "String  \"STOPPED\""
FAILED = "String  \"FAILED\""
STARTING = "String  \"STARTING\""
STARTED = "String  \"STARTED\""
STOPPING = "String  \"STOPPING\""
RUNNING = "String  \"RUNNING\""
def AbstractLifeCycle():
    '''public AbstractLifeCycle()
    '''
def start():
    '''public final void start()
    '''
def stop():
    '''public final void stop()
    '''
def isRunning():
    '''public boolean isRunning()
    '''
def isStarted():
    '''public boolean isStarted()
    '''
def isStarting():
    '''public boolean isStarting()
    '''
def isStopping():
    '''public boolean isStopping()
    '''
def isStopped():
    '''public boolean isStopped()
    '''
def isFailed():
    '''public boolean isFailed()
    '''
def addLifeCycleListener():
    '''public void addLifeCycleListener(final Listener listener)
    '''
def removeLifeCycleListener():
    '''public void removeLifeCycleListener(final Listener listener)
    '''
def getState():
    '''public String getState()
    public static String getState(final LifeCycle lc)
    '''
def lifeCycleFailure():
    '''public void lifeCycleFailure(final LifeCycle event, final Throwable cause)
    '''
def lifeCycleStarted():
    '''public void lifeCycleStarted(final LifeCycle event)
    '''
def lifeCycleStarting():
    '''public void lifeCycleStarting(final LifeCycle event)
    '''
def lifeCycleStopped():
    '''public void lifeCycleStopped(final LifeCycle event)
    '''
def lifeCycleStopping():
    '''public void lifeCycleStopping(final LifeCycle event)
    '''
