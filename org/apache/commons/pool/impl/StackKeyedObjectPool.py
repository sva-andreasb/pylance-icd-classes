def StackKeyedObjectPool():
    '''    public StackKeyedObjectPool()
    public StackKeyedObjectPool(final int max)
    public StackKeyedObjectPool(final int max, final int init)
    public StackKeyedObjectPool(final KeyedPoolableObjectFactory factory)
    public StackKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int max)
    public StackKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int max, final int init)
    '''
def borrowObject():
    '''    public synchronized Object borrowObject(final Object key)
    '''
def returnObject():
    '''    public synchronized void returnObject(final Object key, final Object obj)
    '''
def invalidateObject():
    '''    public synchronized void invalidateObject(final Object key, final Object obj)
    '''
def addObject():
    '''    public synchronized void addObject(final Object key)
    '''
def getNumIdle():
    '''    public synchronized int getNumIdle()
    public synchronized int getNumIdle(final Object key)
    '''
def getNumActive():
    '''    public synchronized int getNumActive()
    public synchronized int getNumActive(final Object key)
    '''
def clear():
    '''    public synchronized void clear()
    public synchronized void clear(final Object key)
    '''
def toString():
    '''    public synchronized String toString()
    '''
def close():
    '''    public void close()
    '''
def setFactory():
    '''    public synchronized void setFactory(final KeyedPoolableObjectFactory factory)
    '''
