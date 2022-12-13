def FileAlterationMonitor():
'''public FileAlterationMonitor()
public FileAlterationMonitor(final long interval)
public FileAlterationMonitor(final long interval, final FileAlterationObserver... observers)
'''
pass
def getInterval():
'''public long getInterval()
'''
pass
def setThreadFactory():
'''public synchronized void setThreadFactory(final ThreadFactory threadFactory)
'''
pass
def addObserver():
'''public void addObserver(final FileAlterationObserver observer)
'''
pass
def removeObserver():
'''public void removeObserver(final FileAlterationObserver observer)
'''
pass
def getObservers():
'''public Iterable<FileAlterationObserver> getObservers()
'''
pass
def start():
'''public synchronized void start()
'''
pass
def stop():
'''public synchronized void stop()
public synchronized void stop(final long stopInterval)
'''
pass
def run():
'''public void run()
'''
pass
