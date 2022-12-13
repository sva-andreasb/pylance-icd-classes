def StackObjectPool():
'''public StackObjectPool()
public StackObjectPool(final int maxIdle)
public StackObjectPool(final int maxIdle, final int initIdleCapacity)
public StackObjectPool(final PoolableObjectFactory factory)
public StackObjectPool(final PoolableObjectFactory factory, final int maxIdle)
public StackObjectPool(final PoolableObjectFactory factory, final int maxIdle, final int initIdleCapacity)
'''
pass
def borrowObject():
'''public synchronized Object borrowObject()
'''
pass
def returnObject():
'''public synchronized void returnObject(Object obj)
'''
pass
def invalidateObject():
'''public synchronized void invalidateObject(final Object obj)
'''
pass
def getNumIdle():
'''public synchronized int getNumIdle()
'''
pass
def getNumActive():
'''public synchronized int getNumActive()
'''
pass
def clear():
'''public synchronized void clear()
'''
pass
def close():
'''public void close()
'''
pass
def addObject():
'''public synchronized void addObject()
'''
pass
def setFactory():
'''public synchronized void setFactory(final PoolableObjectFactory factory)
'''
pass
