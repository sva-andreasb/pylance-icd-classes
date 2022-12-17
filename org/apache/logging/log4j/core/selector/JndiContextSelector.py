def ():
    '''returns JndiContextSelector\n\n
    ()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown(final String fqcn, final ClassLoader loader, final boolean currentContext, final boolean allContexts)\n
    '''
def hasContext():
    '''returns boolean\n\n
    hasContext(final String fqcn, final ClassLoader loader, final boolean currentContext)\n
    '''
def getContext():
    '''returns LoggerContext\n\n
    getContext(final String fqcn, final ClassLoader loader, final boolean currentContext)\n
    getContext(final String fqcn, final ClassLoader loader, final boolean currentContext, final URI configLocation)\n
    '''
def locateContext():
    '''returns LoggerContext\n\n
    locateContext(final String name, final Object externalContext, final URI configLocation)\n
    '''
def removeContext():
    '''returns LoggerContext\n\n
    removeContext(final LoggerContext context)\n
    removeContext(final String name)\n
    '''
def isClassLoaderDependent():
    '''returns boolean\n\n
    isClassLoaderDependent()\n
    '''
def getLoggerContexts():
    '''returns List<LoggerContext>\n\n
    getLoggerContexts()\n
    '''
