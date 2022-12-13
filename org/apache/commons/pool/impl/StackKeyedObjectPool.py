def StackKeyedObjectPool():
'''public StackKeyedObjectPool()
public StackKeyedObjectPool(final int max)
public StackKeyedObjectPool(final int max, final int init)
public StackKeyedObjectPool(final KeyedPoolableObjectFactory factory)
public StackKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int max)
public StackKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int max, final int init)
'''
pass
def borrowObject():
'''public synchronized Object borrowObject(final Object key)
'''
pass
def returnObject():
'''public synchronized void returnObject(final Object key, final Object obj)
'''
pass
def invalidateObject():
'''public synchronized void invalidateObject(final Object key, final Object obj)
'''
pass
def addObject():
'''public synchronized void addObject(final Object key)
'''
pass
def getNumIdle():
'''public synchronized int getNumIdle()
public synchronized int getNumIdle(final Object key)
'''
pass
def getNumActive():
'''public synchronized int getNumActive()
public synchronized int getNumActive(final Object key)
'''
pass
def clear():
'''public synchronized void clear()
public synchronized void clear(final Object key)
'''
pass
def toString():
'''public synchronized String toString()
'''
pass
def close():
'''public void close()
'''
pass
def setFactory():
'''public synchronized void setFactory(final KeyedPoolableObjectFactory factory)
'''
pass
