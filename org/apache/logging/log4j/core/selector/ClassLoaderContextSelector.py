def shutdown():
    '''returns None\n\n
    shutdown(final String fqcn, final ClassLoader loader, final boolean currentContext, final boolean allContexts)\n
    '''
def contextShutdown():
    '''returns None\n\n
    contextShutdown(final org.apache.logging.log4j.spi.LoggerContext loggerContext)\n
    '''
def hasContext():
    '''returns boolean\n\n
    hasContext(final String fqcn, final ClassLoader loader, final boolean currentContext)\n
    '''
def getContext():
    '''returns LoggerContext\n\n
    getContext(final String fqcn, final ClassLoader loader, final boolean currentContext)\n
    getContext(final String fqcn, final ClassLoader loader, final boolean currentContext, final URI configLocation)\n
    getContext(final String fqcn, final ClassLoader loader, final Map.Entry<String, Object> entry, final boolean currentContext, final URI configLocation)\n
    '''
def removeContext():
    '''returns None\n\n
    removeContext(final LoggerContext context)\n
    '''
def isClassLoaderDependent():
    '''returns boolean\n\n
    isClassLoaderDependent()\n
    '''
def getLoggerContexts():
    '''returns List<LoggerContext>\n\n
    getLoggerContexts()\n
    '''
