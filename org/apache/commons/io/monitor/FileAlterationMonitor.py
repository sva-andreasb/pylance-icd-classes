def FileAlterationMonitor():
    '''public FileAlterationMonitor()
    public FileAlterationMonitor(final long interval)
    public FileAlterationMonitor(final long interval, final FileAlterationObserver... observers)
    '''
def getInterval():
    '''public long getInterval()
    '''
def setThreadFactory():
    '''public synchronized void setThreadFactory(final ThreadFactory threadFactory)
    '''
def addObserver():
    '''public void addObserver(final FileAlterationObserver observer)
    '''
def removeObserver():
    '''public void removeObserver(final FileAlterationObserver observer)
    '''
def getObservers():
    '''public Iterable<FileAlterationObserver> getObservers()
    '''
def start():
    '''public synchronized void start()
    '''
def stop():
    '''public synchronized void stop()
    public synchronized void stop(final long stopInterval)
    '''
def run():
    '''public void run()
    '''
