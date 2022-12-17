PROPERTY_CONFIG = "String  \"config\""
def ():
    '''returns LoggerContext\n\n
    (final String name)\n
    (final String name, final Object externalContext)\n
    (final String name, final Object externalContext, final URI configLocn)\n
    (final String name, final Object externalContext, final String configLocn)\n
    '''
def addShutdownListener():
    '''returns None\n\n
    addShutdownListener(final LoggerContextShutdownAware listener)\n
    '''
def getListeners():
    '''returns List<LoggerContextShutdownAware>\n\n
    getListeners()\n
    '''
def start():
    '''returns None\n\n
    start()\n
    start(final Configuration config)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def terminate():
    '''returns None\n\n
    terminate()\n
    '''
def stop():
    '''returns boolean\n\n
    stop(final long timeout, final TimeUnit timeUnit)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getRootLogger():
    '''returns Logger\n\n
    getRootLogger()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getObject():
    '''returns Object\n\n
    getObject(final String key)\n
    '''
def putObject():
    '''returns Object\n\n
    putObject(final String key, final Object value)\n
    '''
def putObjectIfAbsent():
    '''returns Object\n\n
    putObjectIfAbsent(final String key, final Object value)\n
    '''
def removeObject():
    '''returns boolean\n\n
    removeObject(final String key)\n
    removeObject(final String key, final Object value)\n
    '''
def setExternalContext():
    '''returns None\n\n
    setExternalContext(final Object context)\n
    '''
def getExternalContext():
    '''returns Object\n\n
    getExternalContext()\n
    '''
def getLogger():
    '''returns Logger\n\n
    getLogger(final String name)\n
    getLogger(final String name, final MessageFactory messageFactory)\n
    '''
def getLoggers():
    '''returns Collection<Logger>\n\n
    getLoggers()\n
    '''
def hasLogger():
    '''returns boolean\n\n
    hasLogger(final String name)\n
    hasLogger(final String name, final MessageFactory messageFactory)\n
    hasLogger(final String name, final Class<? extends MessageFactory> messageFactoryClass)\n
    '''
def getConfiguration():
    '''returns Configuration\n\n
    getConfiguration()\n
    '''
def addFilter():
    '''returns None\n\n
    addFilter(final Filter filter)\n
    '''
def removeFilter():
    '''returns None\n\n
    removeFilter(final Filter filter)\n
    '''
def setConfiguration():
    '''returns Configuration\n\n
    setConfiguration(final Configuration config)\n
    '''
def addPropertyChangeListener():
    '''returns None\n\n
    addPropertyChangeListener(final PropertyChangeListener listener)\n
    '''
def removePropertyChangeListener():
    '''returns None\n\n
    removePropertyChangeListener(final PropertyChangeListener listener)\n
    '''
def getConfigLocation():
    '''returns URI\n\n
    getConfigLocation()\n
    '''
def setConfigLocation():
    '''returns None\n\n
    setConfigLocation(final URI configLocation)\n
    '''
def reconfigure():
    '''returns None\n\n
    reconfigure()\n
    reconfigure(final Configuration configuration)\n
    '''
def updateLoggers():
    '''returns None\n\n
    updateLoggers()\n
    updateLoggers(final Configuration config)\n
    '''
