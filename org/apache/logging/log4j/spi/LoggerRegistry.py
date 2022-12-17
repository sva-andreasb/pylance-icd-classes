def ():
    '''returns LoggerRegistry\n\n
    ()\n
    (final MapFactory<T> factory)\n
    '''
def getLogger():
    '''returns T\n\n
    getLogger(final String name)\n
    getLogger(final String name, final MessageFactory messageFactory)\n
    '''
def getLoggers():
    '''returns Collection<T>\n\n
    getLoggers()\n
    getLoggers(final Collection<T> destination)\n
    '''
def hasLogger():
    '''returns boolean\n\n
    hasLogger(final String name)\n
    hasLogger(final String name, final MessageFactory messageFactory)\n
    hasLogger(final String name, final Class<? extends MessageFactory> messageFactoryClass)\n
    '''
def putIfAbsent():
    '''returns None\n\n
    putIfAbsent(final String name, final MessageFactory messageFactory, final T logger)\n
    putIfAbsent(final Map<String, T> innerMap, final String name, final T logger)\n
    putIfAbsent(final Map<String, T> innerMap, final String name, final T logger)\n
    '''
