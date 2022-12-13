def shutdown():
    '''    public void shutdown(final String fqcn, final ClassLoader loader, final boolean currentContext, final boolean allContexts)
    '''
def contextShutdown():
    '''    public void contextShutdown(final org.apache.logging.log4j.spi.LoggerContext loggerContext)
    '''
def hasContext():
    '''    public boolean hasContext(final String fqcn, final ClassLoader loader, final boolean currentContext)
    '''
def getContext():
    '''    public LoggerContext getContext(final String fqcn, final ClassLoader loader, final boolean currentContext)
    public LoggerContext getContext(final String fqcn, final ClassLoader loader, final boolean currentContext, final URI configLocation)
    public LoggerContext getContext(final String fqcn, final ClassLoader loader, final Map.Entry<String, Object> entry, final boolean currentContext, final URI configLocation)
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
