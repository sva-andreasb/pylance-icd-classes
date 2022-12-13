def adapt():
'''public static PoolableObjectFactory adapt(final KeyedPoolableObjectFactory keyedFactory)
public static PoolableObjectFactory adapt(final KeyedPoolableObjectFactory keyedFactory, final Object key)
public static KeyedPoolableObjectFactory adapt(final PoolableObjectFactory factory)
public static ObjectPool adapt(final KeyedObjectPool keyedPool)
public static ObjectPool adapt(final KeyedObjectPool keyedPool, final Object key)
public static KeyedObjectPool adapt(final ObjectPool pool)
'''
pass
def checkedPool():
'''public static ObjectPool checkedPool(final ObjectPool pool, final Class type)
public static KeyedObjectPool checkedPool(final KeyedObjectPool keyedPool, final Class type)
'''
pass
def checkMinIdle():
'''public static TimerTask checkMinIdle(final ObjectPool pool, final int minIdle, final long period)
public static TimerTask checkMinIdle(final KeyedObjectPool keyedPool, final Object key, final int minIdle, final long period)
public static Map checkMinIdle(final KeyedObjectPool keyedPool, final Collection keys, final int minIdle, final long period)
'''
pass
def prefill():
'''public static void prefill(final ObjectPool pool, final int count)
public static void prefill(final KeyedObjectPool keyedPool, final Object key, final int count)
public static void prefill(final KeyedObjectPool keyedPool, final Collection keys, final int count)
'''
pass
def synchronizedPool():
'''public static ObjectPool synchronizedPool(final ObjectPool pool)
public static KeyedObjectPool synchronizedPool(final KeyedObjectPool keyedPool)
'''
pass
def synchronizedPoolableFactory():
'''public static PoolableObjectFactory synchronizedPoolableFactory(final PoolableObjectFactory factory)
public static KeyedPoolableObjectFactory synchronizedPoolableFactory(final KeyedPoolableObjectFactory keyedFactory)
'''
pass
def erodingPool():
'''public static ObjectPool erodingPool(final ObjectPool pool)
public static ObjectPool erodingPool(final ObjectPool pool, final float factor)
public static KeyedObjectPool erodingPool(final KeyedObjectPool keyedPool)
public static KeyedObjectPool erodingPool(final KeyedObjectPool keyedPool, final float factor)
public static KeyedObjectPool erodingPool(final KeyedObjectPool keyedPool, final float factor, final boolean perKey)
'''
pass
def makeObject():
'''public Object makeObject()
public Object makeObject(final Object key)
public Object makeObject()
public Object makeObject(final Object key)
'''
pass
def destroyObject():
'''public void destroyObject(final Object obj)
public void destroyObject(final Object key, final Object obj)
public void destroyObject(final Object obj)
public void destroyObject(final Object key, final Object obj)
'''
pass
def validateObject():
'''public boolean validateObject(final Object obj)
public boolean validateObject(final Object key, final Object obj)
public boolean validateObject(final Object obj)
public boolean validateObject(final Object key, final Object obj)
'''
pass
def activateObject():
'''public void activateObject(final Object obj)
public void activateObject(final Object key, final Object obj)
public void activateObject(final Object obj)
public void activateObject(final Object key, final Object obj)
'''
pass
def passivateObject():
'''public void passivateObject(final Object obj)
public void passivateObject(final Object key, final Object obj)
public void passivateObject(final Object obj)
public void passivateObject(final Object key, final Object obj)
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
'''
pass
def borrowObject():
'''public Object borrowObject()
public Object borrowObject(final Object key)
public Object borrowObject()
public Object borrowObject(final Object key)
public Object borrowObject()
public Object borrowObject(final Object key)
public Object borrowObject()
public Object borrowObject(final Object key)
'''
pass
def returnObject():
'''public void returnObject(final Object obj)
public void returnObject(final Object key, final Object obj)
public void returnObject(final Object obj)
public void returnObject(final Object key, final Object obj)
public void returnObject(final Object obj)
public void returnObject(final Object key, final Object obj)
public void returnObject(final Object obj)
public void returnObject(final Object key, final Object obj)
'''
pass
def invalidateObject():
'''public void invalidateObject(final Object obj)
public void invalidateObject(final Object key, final Object obj)
public void invalidateObject(final Object obj)
public void invalidateObject(final Object key, final Object obj)
public void invalidateObject(final Object obj)
public void invalidateObject(final Object key, final Object obj)
public void invalidateObject(final Object obj)
public void invalidateObject(final Object key, final Object obj)
'''
pass
def addObject():
'''public void addObject()
public void addObject(final Object key)
public void addObject()
public void addObject(final Object key)
public void addObject()
public void addObject(final Object key)
public void addObject()
public void addObject(final Object key)
'''
pass
def getNumIdle():
'''public int getNumIdle()
public int getNumIdle(final Object key)
public int getNumIdle()
public int getNumIdle()
public int getNumIdle(final Object key)
public int getNumIdle()
public int getNumIdle()
public int getNumIdle(final Object key)
public int getNumIdle()
public int getNumIdle()
public int getNumIdle()
public int getNumIdle(final Object key)
'''
pass
def getNumActive():
'''public int getNumActive()
public int getNumActive(final Object key)
public int getNumActive()
public int getNumActive()
public int getNumActive(final Object key)
public int getNumActive()
public int getNumActive()
public int getNumActive(final Object key)
public int getNumActive()
public int getNumActive()
public int getNumActive()
public int getNumActive(final Object key)
'''
pass
def clear():
'''public void clear()
public void clear()
public void clear(final Object key)
public void clear()
public void clear()
public void clear(final Object key)
public void clear()
public void clear()
public void clear(final Object key)
public void clear()
public void clear()
public void clear(final Object key)
'''
pass
def close():
'''public void close()
public void close()
public void close()
public void close()
public void close()
public void close()
public void close()
public void close()
'''
pass
def setFactory():
'''public void setFactory(final PoolableObjectFactory factory)
public void setFactory(final KeyedPoolableObjectFactory factory)
public void setFactory(final PoolableObjectFactory factory)
public void setFactory(final KeyedPoolableObjectFactory factory)
public void setFactory(final PoolableObjectFactory factory)
public void setFactory(final KeyedPoolableObjectFactory factory)
public void setFactory(final PoolableObjectFactory factory)
public void setFactory(final KeyedPoolableObjectFactory factory)
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def ErodingFactor():
'''public ErodingFactor(final float factor)
'''
pass
def update():
'''public void update(final int numIdle)
public void update(final long now, final int numIdle)
'''
pass
def getNextShrink():
'''public long getNextShrink()
'''
pass
def ErodingObjectPool():
'''public ErodingObjectPool(final ObjectPool pool, final float factor)
'''
pass
def ErodingKeyedObjectPool():
'''public ErodingKeyedObjectPool(final KeyedObjectPool keyedPool, final float factor)
'''
pass
def ErodingPerKeyKeyedObjectPool():
'''public ErodingPerKeyKeyedObjectPool(final KeyedObjectPool keyedPool, final float factor)
'''
pass
