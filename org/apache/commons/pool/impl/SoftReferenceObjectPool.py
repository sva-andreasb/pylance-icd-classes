def SoftReferenceObjectPool():
    '''    public SoftReferenceObjectPool()
    public SoftReferenceObjectPool(final PoolableObjectFactory factory)
    public SoftReferenceObjectPool(final PoolableObjectFactory factory, final int initSize)
    '''
def borrowObject():
    '''    public synchronized Object borrowObject()
    '''
def returnObject():
    '''    public synchronized void returnObject(final Object obj)
    '''
def invalidateObject():
    '''    public synchronized void invalidateObject(final Object obj)
    '''
def addObject():
    '''    public synchronized void addObject()
    '''
def getNumIdle():
    '''    public synchronized int getNumIdle()
    '''
def getNumActive():
    '''    public synchronized int getNumActive()
    '''
def clear():
    '''    public synchronized void clear()
    '''
def close():
    '''    public void close()
    '''
def setFactory():
    '''    public synchronized void setFactory(final PoolableObjectFactory factory)
    '''
