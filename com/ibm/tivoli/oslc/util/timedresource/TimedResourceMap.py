def TimedResourceMap():
    '''    public TimedResourceMap()
    public TimedResourceMap(final int lifespan, final int terminationInterval)
    public TimedResourceMap(final ConcurrentHashMap<K, SelfTerminatingValue> envoy, final int lifespan, final int terminationInterval)
    '''
def clear():
    '''    public void clear()
    '''
def containsKey():
    '''    public boolean containsKey(final Object key)
    '''
def containsValue():
    '''    public boolean containsValue(final Object value)
    '''
def entrySet():
    '''    public Set<Entry<K, TimedResource>> entrySet()
    '''
def get():
    '''    public TimedResource get(final Object key)
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def keySet():
    '''    public Set<K> keySet()
    '''
def put():
    '''    public TimedResource put(final K key, final TimedResource value)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def putAll():
    '''    public void putAll(final Map<? extends K, ? extends TimedResource> map)
    '''
def remove():
    '''    public TimedResource remove(final Object key)
    '''
def size():
    '''    public int size()
    '''
def values():
    '''    public Collection<TimedResource> values()
    '''
def keys():
    '''    public Enumeration keys()
    '''
def getTerminatorThread():
    '''    public Terminator getTerminatorThread()
    '''
def getTerminatorInterval():
    '''    public int getTerminatorInterval()
    public int getTerminatorInterval()
    '''
def getLifeSpan():
    '''    public int getLifeSpan()
    '''
def setTerminationInterval():
    '''    public void setTerminationInterval(final int terminationInterval)
    public void setTerminationInterval(final long terminationInterval)
    '''
def setLifeSpan():
    '''    public void setLifeSpan(final int timeToLive)
    '''
def setKey():
    '''    public void setKey(final K key)
    '''
def getKey():
    '''    public K getKey()
    '''
def setValue():
    '''    public void setValue(final TimedResource value)
    '''
def getValue():
    '''    public TimedResource getValue()
    '''
def setLastAccessed():
    '''    public void setLastAccessed(final long lastAccessed)
    '''
def getLastAccessed():
    '''    public long getLastAccessed()
    '''
def Terminator():
    '''    public Terminator(final boolean startWorkerThread)
    '''
def run():
    '''    public void run()
    '''
def isThreadRunning():
    '''    public boolean isThreadRunning()
    '''
def stopTerminating():
    '''    public void stopTerminating()
    '''
def startWorkerThread():
    '''    public void startWorkerThread()
    '''
def setLifespan():
    '''    public void setLifespan(final long lifespan)
    '''
def getLifespan():
    '''    public int getLifespan()
    '''
