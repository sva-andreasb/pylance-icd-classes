def ():
    '''returns Terminator\n\n
    ()\n
    (final int lifespan, final int terminationInterval)\n
    (final ConcurrentHashMap<K, SelfTerminatingValue> envoy, final int lifespan, final int terminationInterval)\n
    (final boolean startWorkerThread)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def containsKey():
    '''returns boolean\n\n
    containsKey(final Object key)\n
    '''
def containsValue():
    '''returns boolean\n\n
    containsValue(final Object value)\n
    '''
def get():
    '''returns TimedResource\n\n
    get(final Object key)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def keySet():
    '''returns Set<K>\n\n
    keySet()\n
    '''
def put():
    '''returns TimedResource\n\n
    put(final K key, final TimedResource value)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def putAll():
    '''returns None\n\n
    putAll(final Map<? extends K, ? extends TimedResource> map)\n
    '''
def remove():
    '''returns TimedResource\n\n
    remove(final Object key)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def values():
    '''returns Collection<TimedResource>\n\n
    values()\n
    '''
def keys():
    '''returns Enumeration\n\n
    keys()\n
    '''
def getTerminatorThread():
    '''returns Terminator\n\n
    getTerminatorThread()\n
    '''
def getTerminatorInterval():
    '''returns int\n\n
    getTerminatorInterval()\n
    getTerminatorInterval()\n
    '''
def getLifeSpan():
    '''returns int\n\n
    getLifeSpan()\n
    '''
def setTerminationInterval():
    '''returns None\n\n
    setTerminationInterval(final int terminationInterval)\n
    setTerminationInterval(final long terminationInterval)\n
    '''
def setLifeSpan():
    '''returns None\n\n
    setLifeSpan(final int timeToLive)\n
    '''
def setKey():
    '''returns None\n\n
    setKey(final K key)\n
    '''
def getKey():
    '''returns K\n\n
    getKey()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final TimedResource value)\n
    '''
def getValue():
    '''returns TimedResource\n\n
    getValue()\n
    '''
def setLastAccessed():
    '''returns None\n\n
    setLastAccessed(final long lastAccessed)\n
    '''
def getLastAccessed():
    '''returns long\n\n
    getLastAccessed()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def isThreadRunning():
    '''returns boolean\n\n
    isThreadRunning()\n
    '''
def stopTerminating():
    '''returns None\n\n
    stopTerminating()\n
    '''
def startWorkerThread():
    '''returns None\n\n
    startWorkerThread()\n
    '''
def setLifespan():
    '''returns None\n\n
    setLifespan(final long lifespan)\n
    '''
def getLifespan():
    '''returns int\n\n
    getLifespan()\n
    '''
