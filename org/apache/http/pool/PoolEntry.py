def PoolEntry():
    '''    public PoolEntry(final String id, final T route, final C conn, final long timeToLive, final TimeUnit tunit)
    public PoolEntry(final String id, final T route, final C conn)
    '''
def getId():
    '''    public String getId()
    '''
def getRoute():
    '''    public T getRoute()
    '''
def getConnection():
    '''    public C getConnection()
    '''
def getCreated():
    '''    public long getCreated()
    '''
def getValidityDeadline():
    '''    public long getValidityDeadline()
    '''
def getValidUnit():
    '''    public long getValidUnit()
    '''
def getState():
    '''    public Object getState()
    '''
def setState():
    '''    public void setState(final Object state)
    '''
def getUpdated():
    '''    public synchronized long getUpdated()
    '''
def getExpiry():
    '''    public synchronized long getExpiry()
    '''
def updateExpiry():
    '''    public synchronized void updateExpiry(final long time, final TimeUnit tunit)
    '''
def isExpired():
    '''    public synchronized boolean isExpired(final long now)
    '''
def toString():
    '''    public String toString()
    '''
