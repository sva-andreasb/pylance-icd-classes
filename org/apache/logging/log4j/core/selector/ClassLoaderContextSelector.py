def shutdown():
'''public void shutdown(final String fqcn, final ClassLoader loader, final boolean currentContext, final boolean allContexts)
'''
pass
def contextShutdown():
'''public void contextShutdown(final org.apache.logging.log4j.spi.LoggerContext loggerContext)
'''
pass
def hasContext():
'''public boolean hasContext(final String fqcn, final ClassLoader loader, final boolean currentContext)
'''
pass
def getContext():
'''public LoggerContext getContext(final String fqcn, final ClassLoader loader, final boolean currentContext)
public LoggerContext getContext(final String fqcn, final ClassLoader loader, final boolean currentContext, final URI configLocation)
public LoggerContext getContext(final String fqcn, final ClassLoader loader, final Map.Entry<String, Object> entry, final boolean currentContext, final URI configLocation)
'''
pass
def removeContext():
'''public void removeContext(final LoggerContext context)
'''
pass
def isClassLoaderDependent():
'''public boolean isClassLoaderDependent()
'''
pass
def getLoggerContexts():
'''public List<LoggerContext> getLoggerContexts()
'''
pass
