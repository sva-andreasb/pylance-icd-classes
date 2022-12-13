def LoggerRegistry():
'''public LoggerRegistry()
public LoggerRegistry(final MapFactory<T> factory)
'''
pass
def getLogger():
'''public T getLogger(final String name)
public T getLogger(final String name, final MessageFactory messageFactory)
'''
pass
def getLoggers():
'''public Collection<T> getLoggers()
public Collection<T> getLoggers(final Collection<T> destination)
'''
pass
def hasLogger():
'''public boolean hasLogger(final String name)
public boolean hasLogger(final String name, final MessageFactory messageFactory)
public boolean hasLogger(final String name, final Class<? extends MessageFactory> messageFactoryClass)
'''
pass
def putIfAbsent():
'''public void putIfAbsent(final String name, final MessageFactory messageFactory, final T logger)
public void putIfAbsent(final Map<String, T> innerMap, final String name, final T logger)
public void putIfAbsent(final Map<String, T> innerMap, final String name, final T logger)
'''
pass
def createInnerMap():
'''public Map<String, T> createInnerMap()
public Map<String, T> createInnerMap()
'''
pass
def createOuterMap():
'''public Map<String, Map<String, T>> createOuterMap()
public Map<String, Map<String, T>> createOuterMap()
'''
pass
