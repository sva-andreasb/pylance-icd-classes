def SelectChannelEndPoint():
    '''    public SelectChannelEndPoint(final SocketChannel channel, final SelectorManager.SelectSet selectSet, final SelectionKey key, final int maxIdleTime)
    '''
def run():
    '''    public void run()
    '''
def getSelectionKey():
    '''    public SelectionKey getSelectionKey()
    '''
def getSelectManager():
    '''    public SelectorManager getSelectManager()
    '''
def getConnection():
    '''    public Connection getConnection()
    '''
def setConnection():
    '''    public void setConnection(final Connection connection)
    '''
def getIdleTimestamp():
    '''    public long getIdleTimestamp()
    '''
def schedule():
    '''    public void schedule()
    '''
def asyncDispatch():
    '''    public void asyncDispatch()
    '''
def dispatch():
    '''    public void dispatch()
    '''
def cancelTimeout():
    '''    public void cancelTimeout(final Timeout.Task task)
    '''
def scheduleTimeout():
    '''    public void scheduleTimeout(final Timeout.Task task, final long timeoutMs)
    '''
def setCheckForIdle():
    '''    public void setCheckForIdle(final boolean check)
    '''
def isCheckForIdle():
    '''    public boolean isCheckForIdle()
    '''
def checkIdleTimestamp():
    '''    public void checkIdleTimestamp(final long now)
    '''
def onIdleExpired():
    '''    public void onIdleExpired(final long idleForMs)
    '''
def fill():
    '''    public int fill(final Buffer buffer)
    '''
def flush():
    '''    public int flush(final Buffer header, final Buffer buffer, final Buffer trailer)
    public int flush(final Buffer buffer)
    '''
def blockReadable():
    '''    public boolean blockReadable(final long timeoutMs)
    '''
def blockWritable():
    '''    public boolean blockWritable(final long timeoutMs)
    '''
def scheduleWrite():
    '''    public void scheduleWrite()
    '''
def isWritable():
    '''    public boolean isWritable()
    '''
def hasProgressed():
    '''    public boolean hasProgressed()
    '''
def close():
    '''    public void close()
    '''
def toString():
    '''    public String toString()
    '''
def setMaxIdleTime():
    '''    public void setMaxIdleTime(final int timeMs)
    '''
