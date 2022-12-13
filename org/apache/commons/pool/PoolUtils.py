def adapt():
    '''    public static PoolableObjectFactory adapt(final KeyedPoolableObjectFactory keyedFactory)
    public static PoolableObjectFactory adapt(final KeyedPoolableObjectFactory keyedFactory, final Object key)
    public static KeyedPoolableObjectFactory adapt(final PoolableObjectFactory factory)
    public static ObjectPool adapt(final KeyedObjectPool keyedPool)
    public static ObjectPool adapt(final KeyedObjectPool keyedPool, final Object key)
    public static KeyedObjectPool adapt(final ObjectPool pool)
    '''
def checkedPool():
    '''    public static ObjectPool checkedPool(final ObjectPool pool, final Class type)
    public static KeyedObjectPool checkedPool(final KeyedObjectPool keyedPool, final Class type)
    '''
def checkMinIdle():
    '''    public static TimerTask checkMinIdle(final ObjectPool pool, final int minIdle, final long period)
    public static TimerTask checkMinIdle(final KeyedObjectPool keyedPool, final Object key, final int minIdle, final long period)
    public static Map checkMinIdle(final KeyedObjectPool keyedPool, final Collection keys, final int minIdle, final long period)
    '''
def prefill():
    '''    public static void prefill(final ObjectPool pool, final int count)
    public static void prefill(final KeyedObjectPool keyedPool, final Object key, final int count)
    public static void prefill(final KeyedObjectPool keyedPool, final Collection keys, final int count)
    '''
def synchronizedPool():
    '''    public static ObjectPool synchronizedPool(final ObjectPool pool)
    public static KeyedObjectPool synchronizedPool(final KeyedObjectPool keyedPool)
    '''
def synchronizedPoolableFactory():
    '''    public static PoolableObjectFactory synchronizedPoolableFactory(final PoolableObjectFactory factory)
    public static KeyedPoolableObjectFactory synchronizedPoolableFactory(final KeyedPoolableObjectFactory keyedFactory)
    '''
def erodingPool():
    '''    public static ObjectPool erodingPool(final ObjectPool pool)
    public static ObjectPool erodingPool(final ObjectPool pool, final float factor)
    public static KeyedObjectPool erodingPool(final KeyedObjectPool keyedPool)
    public static KeyedObjectPool erodingPool(final KeyedObjectPool keyedPool, final float factor)
    public static KeyedObjectPool erodingPool(final KeyedObjectPool keyedPool, final float factor, final boolean perKey)
    '''
def makeObject():
    '''    public Object makeObject()
    public Object makeObject(final Object key)
    public Object makeObject()
    public Object makeObject(final Object key)
    '''
def destroyObject():
    '''    public void destroyObject(final Object obj)
    public void destroyObject(final Object key, final Object obj)
    public void destroyObject(final Object obj)
    public void destroyObject(final Object key, final Object obj)
    '''
def validateObject():
    '''    public boolean validateObject(final Object obj)
    public boolean validateObject(final Object key, final Object obj)
    public boolean validateObject(final Object obj)
    public boolean validateObject(final Object key, final Object obj)
    '''
def activateObject():
    '''    public void activateObject(final Object obj)
    public void activateObject(final Object key, final Object obj)
    public void activateObject(final Object obj)
    public void activateObject(final Object key, final Object obj)
    '''
def passivateObject():
    '''    public void passivateObject(final Object obj)
    public void passivateObject(final Object key, final Object obj)
    public void passivateObject(final Object obj)
    public void passivateObject(final Object key, final Object obj)
    '''
def toString():
    '''    public String toString()
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
def borrowObject():
    '''    public Object borrowObject()
    public Object borrowObject(final Object key)
    public Object borrowObject()
    public Object borrowObject(final Object key)
    public Object borrowObject()
    public Object borrowObject(final Object key)
    public Object borrowObject()
    public Object borrowObject(final Object key)
    '''
def returnObject():
    '''    public void returnObject(final Object obj)
    public void returnObject(final Object key, final Object obj)
    public void returnObject(final Object obj)
    public void returnObject(final Object key, final Object obj)
    public void returnObject(final Object obj)
    public void returnObject(final Object key, final Object obj)
    public void returnObject(final Object obj)
    public void returnObject(final Object key, final Object obj)
    '''
def invalidateObject():
    '''    public void invalidateObject(final Object obj)
    public void invalidateObject(final Object key, final Object obj)
    public void invalidateObject(final Object obj)
    public void invalidateObject(final Object key, final Object obj)
    public void invalidateObject(final Object obj)
    public void invalidateObject(final Object key, final Object obj)
    public void invalidateObject(final Object obj)
    public void invalidateObject(final Object key, final Object obj)
    '''
def addObject():
    '''    public void addObject()
    public void addObject(final Object key)
    public void addObject()
    public void addObject(final Object key)
    public void addObject()
    public void addObject(final Object key)
    public void addObject()
    public void addObject(final Object key)
    '''
def getNumIdle():
    '''    public int getNumIdle()
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
def getNumActive():
    '''    public int getNumActive()
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
def clear():
    '''    public void clear()
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
def close():
    '''    public void close()
    public void close()
    public void close()
    public void close()
    public void close()
    public void close()
    public void close()
    public void close()
    '''
def setFactory():
    '''    public void setFactory(final PoolableObjectFactory factory)
    public void setFactory(final KeyedPoolableObjectFactory factory)
    public void setFactory(final PoolableObjectFactory factory)
    public void setFactory(final KeyedPoolableObjectFactory factory)
    public void setFactory(final PoolableObjectFactory factory)
    public void setFactory(final KeyedPoolableObjectFactory factory)
    public void setFactory(final PoolableObjectFactory factory)
    public void setFactory(final KeyedPoolableObjectFactory factory)
    '''
def run():
    '''    public void run()
    public void run()
    '''
def ErodingFactor():
    '''    public ErodingFactor(final float factor)
    '''
def update():
    '''    public void update(final int numIdle)
    public void update(final long now, final int numIdle)
    '''
def getNextShrink():
    '''    public long getNextShrink()
    '''
def ErodingObjectPool():
    '''    public ErodingObjectPool(final ObjectPool pool, final float factor)
    '''
def ErodingKeyedObjectPool():
    '''    public ErodingKeyedObjectPool(final KeyedObjectPool keyedPool, final float factor)
    '''
def ErodingPerKeyKeyedObjectPool():
    '''    public ErodingPerKeyKeyedObjectPool(final KeyedObjectPool keyedPool, final float factor)
    '''
