STOPPED = "String  STOPPED""
FAILED = "String  FAILED""
STARTING = "String  STARTING""
STARTED = "String  STARTED""
STOPPING = "String  STOPPING""
RUNNING = "String  RUNNING""
def AbstractLifeCycle():
'''public AbstractLifeCycle()
'''
pass
def start():
'''public final void start()
'''
pass
def stop():
'''public final void stop()
'''
pass
def isRunning():
'''public boolean isRunning()
'''
pass
def isStarted():
'''public boolean isStarted()
'''
pass
def isStarting():
'''public boolean isStarting()
'''
pass
def isStopping():
'''public boolean isStopping()
'''
pass
def isStopped():
'''public boolean isStopped()
'''
pass
def isFailed():
'''public boolean isFailed()
'''
pass
def addLifeCycleListener():
'''public void addLifeCycleListener(final Listener listener)
'''
pass
def removeLifeCycleListener():
'''public void removeLifeCycleListener(final Listener listener)
'''
pass
def getState():
'''public String getState()
public static String getState(final LifeCycle lc)
'''
pass
def lifeCycleFailure():
'''public void lifeCycleFailure(final LifeCycle event, final Throwable cause)
'''
pass
def lifeCycleStarted():
'''public void lifeCycleStarted(final LifeCycle event)
'''
pass
def lifeCycleStarting():
'''public void lifeCycleStarting(final LifeCycle event)
'''
pass
def lifeCycleStopped():
'''public void lifeCycleStopped(final LifeCycle event)
'''
pass
def lifeCycleStopping():
'''public void lifeCycleStopping(final LifeCycle event)
'''
pass
