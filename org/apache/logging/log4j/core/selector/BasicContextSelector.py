def shutdown():
    '''    public void shutdown(final String fqcn, final ClassLoader loader, final boolean currentContext, final boolean allContexts)
    '''
def hasContext():
    '''    public boolean hasContext(final String fqcn, final ClassLoader loader, final boolean currentContext)
    '''
def getContext():
    '''    public LoggerContext getContext(final String fqcn, final ClassLoader loader, final boolean currentContext)
    public LoggerContext getContext(final String fqcn, final ClassLoader loader, final boolean currentContext, final URI configLocation)
    '''
def locateContext():
    '''    public LoggerContext locateContext(final String name, final String configLocation)
    '''
def removeContext():
    '''    public void removeContext(final LoggerContext context)
    '''
def isClassLoaderDependent():
    '''    public boolean isClassLoaderDependent()
    '''
def getLoggerContexts():
    '''    public List<LoggerContext> getLoggerContexts()
    '''
