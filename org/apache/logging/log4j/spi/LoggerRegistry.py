def LoggerRegistry():
    '''    public LoggerRegistry()
    public LoggerRegistry(final MapFactory<T> factory)
    '''
def getLogger():
    '''    public T getLogger(final String name)
    public T getLogger(final String name, final MessageFactory messageFactory)
    '''
def getLoggers():
    '''    public Collection<T> getLoggers()
    public Collection<T> getLoggers(final Collection<T> destination)
    '''
def hasLogger():
    '''    public boolean hasLogger(final String name)
    public boolean hasLogger(final String name, final MessageFactory messageFactory)
    public boolean hasLogger(final String name, final Class<? extends MessageFactory> messageFactoryClass)
    '''
def putIfAbsent():
    '''    public void putIfAbsent(final String name, final MessageFactory messageFactory, final T logger)
    public void putIfAbsent(final Map<String, T> innerMap, final String name, final T logger)
    public void putIfAbsent(final Map<String, T> innerMap, final String name, final T logger)
    '''
def createInnerMap():
    '''    public Map<String, T> createInnerMap()
    public Map<String, T> createInnerMap()
    '''
def createOuterMap():
    '''    public Map<String, Map<String, T>> createOuterMap()
    public Map<String, Map<String, T>> createOuterMap()
    '''
