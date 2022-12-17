def ():
    '''returns Log4jContextFactory\n\n
    ()\n
    (final ContextSelector selector)\n
    (final ShutdownCallbackRegistry shutdownCallbackRegistry)\n
    (final ContextSelector selector, final ShutdownCallbackRegistry shutdownCallbackRegistry)\n
    '''
def getContext():
    '''returns LoggerContext\n\n
    getContext(final String fqcn, final ClassLoader loader, final Object externalContext, final boolean currentContext)\n
    getContext(final String fqcn, final ClassLoader loader, final Object externalContext, final boolean currentContext, final ConfigurationSource source)\n
    getContext(final String fqcn, final ClassLoader loader, final Object externalContext, final boolean currentContext, final Configuration configuration)\n
    getContext(final String fqcn, final ClassLoader loader, final Object externalContext, final boolean currentContext, final URI configLocation, final String name)\n
    getContext(final String fqcn, final ClassLoader loader, final Map.Entry<String, Object> entry, final boolean currentContext, final URI configLocation, final String name)\n
    getContext(final String fqcn, final ClassLoader loader, final Object externalContext, final boolean currentContext, final List<URI> configLocations, final String name)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown(final String fqcn, final ClassLoader loader, final boolean currentContext, final boolean allContexts)\n
    '''
def hasContext():
    '''returns boolean\n\n
    hasContext(final String fqcn, final ClassLoader loader, final boolean currentContext)\n
    '''
def getSelector():
    '''returns ContextSelector\n\n
    getSelector()\n
    '''
def getShutdownCallbackRegistry():
    '''returns ShutdownCallbackRegistry\n\n
    getShutdownCallbackRegistry()\n
    '''
def removeContext():
    '''returns None\n\n
    removeContext(final org.apache.logging.log4j.spi.LoggerContext context)\n
    '''
def isClassLoaderDependent():
    '''returns boolean\n\n
    isClassLoaderDependent()\n
    '''
def addShutdownCallback():
    '''returns Cancellable\n\n
    addShutdownCallback(final Runnable callback)\n
    '''
def isShutdownHookEnabled():
    '''returns boolean\n\n
    isShutdownHookEnabled()\n
    '''
