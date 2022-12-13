DEFAULT_MAX_THREADS = "int  100"
def ThreadPool():
'''public ThreadPool()
public ThreadPool(final int maxPoolSize)
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def isShutdown():
'''public boolean isShutdown()
'''
pass
def isShuttingDown():
'''public boolean isShuttingDown()
'''
pass
def getWorkerCount():
'''public long getWorkerCount()
'''
pass
def addWorker():
'''public void addWorker(final Runnable worker)
'''
pass
def interruptAll():
'''public void interruptAll()
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def safeShutdown():
'''public void safeShutdown()
'''
pass
def awaitShutdown():
'''public synchronized void awaitShutdown()
public synchronized boolean awaitShutdown(final long timeout)
'''
pass
def workerDone():
'''public void workerDone(final Runnable worker, final boolean restart)
'''
pass
