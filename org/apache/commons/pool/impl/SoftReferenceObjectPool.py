def SoftReferenceObjectPool():
'''public SoftReferenceObjectPool()
public SoftReferenceObjectPool(final PoolableObjectFactory factory)
public SoftReferenceObjectPool(final PoolableObjectFactory factory, final int initSize)
'''
pass
def borrowObject():
'''public synchronized Object borrowObject()
'''
pass
def returnObject():
'''public synchronized void returnObject(final Object obj)
'''
pass
def invalidateObject():
'''public synchronized void invalidateObject(final Object obj)
'''
pass
def addObject():
'''public synchronized void addObject()
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
def setFactory():
'''public synchronized void setFactory(final PoolableObjectFactory factory)
'''
pass
