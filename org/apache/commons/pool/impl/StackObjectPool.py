def StackObjectPool():
    '''public StackObjectPool()
    public StackObjectPool(final int maxIdle)
    public StackObjectPool(final int maxIdle, final int initIdleCapacity)
    public StackObjectPool(final PoolableObjectFactory factory)
    public StackObjectPool(final PoolableObjectFactory factory, final int maxIdle)
    public StackObjectPool(final PoolableObjectFactory factory, final int maxIdle, final int initIdleCapacity)
    '''
def borrowObject():
    '''public synchronized Object borrowObject()
    '''
def returnObject():
    '''public synchronized void returnObject(Object obj)
    '''
def invalidateObject():
    '''public synchronized void invalidateObject(final Object obj)
    '''
def getNumIdle():
    '''public synchronized int getNumIdle()
    '''
def getNumActive():
    '''public synchronized int getNumActive()
    '''
def clear():
    '''public synchronized void clear()
    '''
def close():
    '''public void close()
    '''
def addObject():
    '''public synchronized void addObject()
    '''
def setFactory():
    '''public synchronized void setFactory(final PoolableObjectFactory factory)
    '''
